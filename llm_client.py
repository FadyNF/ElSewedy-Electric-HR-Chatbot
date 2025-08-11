import os
import uuid
import logging
from typing import Dict, Generator, List
from datetime import datetime
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from rag_system import RAGSystem
load_dotenv("config.env")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LLMClient:
    """Streamlined LLM Client using LangChain ConversationalRetrievalChain.""" 
    def __init__(self):
        # LLM Configuration
        self.api_key = os.getenv("API_KEY")
        self.model = os.getenv("MODEL", "gpt-4o")
        
        # System prompt (maintainable string)
        self.system_prompt = (
            "You are an HR Assistant for Elsewedy Electric, your primary role is to answer questions based on the provided company policies. When relevant policy context is available, use it to respond. If the context only contains references to other policies (like 'Refer to Policy X'), acknowledge the reference and ask the user to be more specific about what aspect of the policy they need help with. If no relevant context is provided for a specific question, state, I don't have that information in the provided policies. Always try to guide the user to an answer related to the HR policies that we have available. DO NOT USE external knowledge about Elsewedy or other companies not explicitly provided in the context. \n\n"
            "LANGUAGE HANDLING:\n\n"
            "- If spoken to in Arabic (العربية), respond in Egyptian Arabic  \n"
            "- If spoken to in English, respond in English  \n"
            "- Search for policy information in both Arabic and English content  \n"
            "- If a policy name is mentioned in Arabic, search for both Arabic and English versions  \n\n"
            "EXAMPLES:\n\n"
            "English Example 1:  \n"
            "Question: What is the dress code for office employees at Elsewedy Electric?  \n"
            "Answer: Based on the Dress Code & Personal Appearance Policy, for offices, employees are required to wear formal or semi-formal attire, including suits, jackets, shirts, skirts, and pants typical of formal business attire. All clothing should be neat, without tears, revealing, rips, or holes, and should not be revealing or have offensive stamps or prints. On Thursdays, smart casual wear is accepted, including jeans, polo shirts, t-shirts (no drawings), and sneakers, but slippers, shorts, ripped jeans, and sportswear are not allowed. Females are allowed to wear jewelry, but visible body piercings are not permitted during working hours. Employees must maintain personal hygiene, including neat haircuts, trimmed beards, and proper nail care.\n\n"
            "English Example 2:  \n"
            "Question: What is the Requisition Process?  \n"
            "Answer: The requisition process involves the following steps:\n"
            "1. Hiring Manager opens the job requisition on TALEO.\n"
            "2. Head of Department approves the job requisition.\n"
            "3. Sector/Country Organization Design reviews the business need (especially if unplanned), drafts/revises the Job Description (JD), and proposes the job level.\n"
            "4. Group Organization Design validates the BU structure, confirms the need, approves the JD, and performs job evaluation if needed to confirm the proposed level and job title.\n"
            "5. Group Total Rewards sets the compensation package, including salary range and all other applicable rewards, based on the finalized job level.\n"
            "6. BU HRBP reviews and approves the full job requisition and attached details. (In case of an ad-hoc request, not approved in the manpower plan)\n"
            "7. BU Head gives final approval on the job requisition. (In case of an ad-hoc request, not approved in the manpower plan)\n\n"
            "Arabic Example 1:  \n"
            "السؤال: إيه هي سياسة السلف في الشركة؟  \n"
            "الإجابة: على حسب سياسة سلف العاملين، الموظفين ليهم حق ياخدوا سُلف بشروط وأحكام معينة مذكورة في السياسة. لازم يقدموا طلب السلفة بالطريقة المعتمدة وياخدوا الموافقات المطلوبة من الإدارة المختصة.\n\n"
            "Arabic Example 2:  \n"
            "السؤال: أعمل إيه علشان أترقى؟  \n"
            "الإجابة: على حسب سياسة الترقيات، الترقية للدرجة الأعلى بتتطلب إن الموظف يكون متصنف كموظف عالي الإمكانيات (HIPO) من خلال اجتماع مراجعة المواهب ومركز تقييم المواهب. المعايير بتشمل:  \n"
            "١. وجود هيكل تنظيمي معتمد  \n"
            "٢. وجود وظيفة متاحة في الدرجة المطلوبة  \n"
            "٣. وجود ميزانية متاحة  \n"
            "٤. جاهزية الموظف المرشح (HIPO)  \n"
            "٥. موافقة رئيس القطاع أو وحدة العمل  \n"
            "وبالنسبة للوظايف القيادية، محتاجين كمان موافقة الـ CHRO وCEO للمجموعة. \n\n"
        )     
        # Initialize OpenAI client with streaming
        self.llm = ChatOpenAI(
            base_url="https://models.inference.ai.azure.com",
            api_key=self.api_key,
            model=self.model,
            temperature=0.1,
            max_tokens=2000,
            streaming=True
        )
        
        # Initialize RAG system
        self.rag_system = RAGSystem()
        
        # In-memory sessions: session_id -> {"title": str, "chain": ConversationalRetrievalChain}
        self.sessions: Dict[str, Dict] = {}

    def _get_prompt_template(self):
        """Get the prompt template with system prompt."""
        template = f"""{self.system_prompt}

Context from company policies:
{{context}}

Chat History:
{{chat_history}}

Question: {{question}}
Answer:"""
        
        return PromptTemplate(
            input_variables=["context", "chat_history", "question"],
            template=template
        )

    def create_session(self, title: str = None) -> str:
        """Create a new chat session with its own conversation chain."""
        session_id = str(uuid.uuid4())
        
        if not title:
            title = f"Chat Session {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        
        # Create memory for this session
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )
        
        # Create conversation chain for this session
        chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.rag_system.get_retriever(),
            memory=memory,
            return_source_documents=False,  # No citations needed
            combine_docs_chain_kwargs={
                "prompt": self._get_prompt_template()
            }
        )
        
        self.sessions[session_id] = {
            "title": title,
            "updated_at": datetime.now(),
            "chain": chain
        }
        
        logger.info(f"Created new session: {session_id}")
        return session_id

    def get_session_messages(self, session_id: str, limit: int = 50) -> List[Dict]:
        """Get messages for a session from memory."""
        session = self.sessions.get(session_id)
        if not session:
            return []
        
        try:
            memory = session["chain"].memory
            messages = memory.chat_memory.messages[-limit * 2:]  # *2 because we have user+assistant pairs
            
            result = []
            for i in range(0, len(messages), 2):
                if i + 1 < len(messages):
                    user_msg = messages[i]
                    assistant_msg = messages[i + 1]
                    result.append({"role": "user", "content": user_msg.content})
                    result.append({"role": "assistant", "content": assistant_msg.content})
            
            return result[-limit:]  # Final limit
        except Exception as e:
            logger.error(f"Error getting session messages: {e}")
            return []

    def save_message(self, session_id: str, role: str, content: str, 
                    rag_context: str = None, similarity_score: float = None):
        """Save message - now handled automatically by LangChain memory."""
        # This method is kept for compatibility but LangChain handles saving automatically
        session = self.sessions.get(session_id)
        if session:
            session["updated_at"] = datetime.now()

    def list_sessions(self, limit: int = 5) -> List[Dict]:
        """List recent chat sessions."""
        items = [
            {
                "id": sid,
                "title": data.get("title", "Untitled"),
                "updated_at": data.get("updated_at"),
            }
            for sid, data in self.sessions.items()
        ]
        items.sort(key=lambda x: x["updated_at"] or datetime.fromtimestamp(0), reverse=True)
        return items[:limit]

    def delete_session(self, session_id: str) -> bool:
        """Delete a chat session."""
        return self.sessions.pop(session_id, None) is not None

    def update_session_title(self, session_id: str, title: str):
        """Update session title."""
        if session_id in self.sessions:
            self.sessions[session_id]["title"] = title
            self.sessions[session_id]["updated_at"] = datetime.now()

    def _retry_with_fallback(self, chain, question: str, max_retries: int = 3) -> Generator[str, None, None]:
        """Execute chain with retry logic and fallback."""
        for attempt in range(max_retries):
            try:
                # Stream the response directly
                for chunk in chain.stream({"question": question}):
                    if "answer" in chunk:
                        yield chunk["answer"]
                
                return  # Success, exit retry loop
                
            except Exception as e:
                logger.error(f"Attempt {attempt + 1} failed: {e}")
                if attempt == max_retries - 1:
                    # Final attempt failed, yield error message
                    yield "I apologize, but the model is currently unavailable. Please try again later."
                    return

    def chat(self, session_id: str, user_message: str) -> Dict:
        """Handle chat interaction with streaming (always)."""
        try:
            # Get or create session
            if session_id not in self.sessions:
                self.create_session()
            
            session = self.sessions[session_id]
            chain = session["chain"]
            
            # Update session title if it's the first message
            memory_messages = chain.memory.chat_memory.messages
            if len(memory_messages) == 0:
                title = user_message[:50] + ("..." if len(user_message) > 50 else "")
                self.update_session_title(session_id, title)
            
            # Create streaming generator with retry logic
            def streaming_generator():
                full_response = ""
                for chunk in self._retry_with_fallback(chain, user_message):
                    full_response += chunk
                    yield chunk
                
                # Update session timestamp after completion
                session["updated_at"] = datetime.now()
            
            return {
                'stream': streaming_generator(),
                'used_rag': True,  # Always true with ConversationalRetrievalChain
                'similarity_score': 1.0  # LangChain handles retrieval internally
            }
            
        except Exception as e:
            logger.error(f"Error in chat interaction: {e}")
            
            def error_generator():
                yield "I apologize, but I encountered an error. Please try again."
            
            return {
                'stream': error_generator(),
                'used_rag': False,
                'similarity_score': 0.0
            }


if __name__ == "__main__":
    # Test the LLM client
    llm = LLMClient()
    session_id = llm.create_session()
    result = llm.chat(session_id, "What is the dress code?")
    
    print("Response:")
    for chunk in result['stream']:
        print(chunk, end="", flush=True)
    print()