import os
import uuid
import logging
from typing import Callable, List, Dict, Optional, Tuple, Union, Generator
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
import psycopg2
from psycopg2.extras import RealDictCursor
import warnings
from rag_system import RAGSystem
import re

# Load environment variables
load_dotenv("config.env")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LLMClient:
    """LLM Client with RAG integration and chat session management."""
    
    def __init__(self):
        # LLM Configuration
        self.api_key = os.getenv("API_KEY")
        self.model = os.getenv("MODEL", "gpt-4o")
        self.similarity_threshold = float(os.getenv("SIMILARITY_THRESHOLD", "0.55")) 
        
        # database configuration
        self.db_config = {
            'host': os.getenv('PGHOST', 'localhost'),
            'port': int(os.getenv('PGPORT', '5433')),
            'database': os.getenv('PGDATABASE', 'test'),
            'user': os.getenv('PGUSER', 'postgres'),
            'password': os.getenv('PGPASSWORD', 'password')
        }
        
        # initialize clients (we can change this depending on what API we use. qwen-3 is fine but needs a change in system prompt.)
        self.client = OpenAI(
            base_url="https://models.inference.ai.azure.com",
            api_key=self.api_key
        )
        
        # initialize RAG system
        self.rag_system = RAGSystem()
        
        # System prompt
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
        
    def _get_connection(self):
        """Get database connection."""
        return psycopg2.connect(**self.db_config)
    
    def create_session(self, title: str = None) -> str:
        """Create a new chat session."""
        session_id = str(uuid.uuid4())
        
        if not title:
            title = f"Chat Session {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        
        try:
            with self._get_connection() as conn:
                with conn.cursor() as eng:
                    eng.execute(
                        "INSERT INTO chat_sessions (id, title) VALUES (%s, %s)",
                        (session_id, title)
                    )
                    conn.commit()
            
            logger.info(f"Created new session: {session_id}")
            return session_id
        except Exception as e:
            logger.error(f"Error creating session: {e}")
            raise
    
    def get_session_messages(self, session_id: str, limit: int = 50) -> List[Dict]:
        """Get messages for a session."""
        try:
            with self._get_connection() as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as eng:
                    eng.execute("""
                        SELECT role, content, rag_context, similarity_score, created_at
                        FROM chat_messages 
                        WHERE session_id = %s 
                        ORDER BY created_at ASC 
                        LIMIT %s
                    """, (session_id, limit))
                    
                    messages = []
                    for row in eng.fetchall():
                        messages.append({
                            'role': row['role'],
                            'content': row['content'],
                            'rag_context': row['rag_context'],
                            'similarity_score': row['similarity_score'],
                            'created_at': row['created_at']
                        })
                    
                    return messages
        except Exception as e:
            logger.error(f"Error getting session messages: {e}")
            return []
    
    def save_message(self, session_id: str, role: str, content: str, 
                    rag_context: str = None, similarity_score: float = None):
        """Save a message to the database."""
        try:
            with self._get_connection() as conn:
                with conn.cursor() as eng:
                    eng.execute("""
                        INSERT INTO chat_messages 
                        (session_id, role, content, rag_context, similarity_score) 
                        VALUES (%s, %s, %s, %s, %s)
                    """, (session_id, role, content, rag_context, similarity_score))
                    
                    conn.commit()
        except Exception as e:
            logger.error(f"Error saving message: {e}")
            raise
    
    def list_sessions(self, limit: int = 5) -> List[Dict]:
        """List recent chat sessions."""
        try:
            with self._get_connection() as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as eng:
                    eng.execute("""
                        SELECT s.id, s.title, COALESCE(MAX(m.created_at), '1970-01-01'::timestamp) as updated_at
                        FROM chat_sessions s
                        LEFT JOIN chat_messages m ON s.id = m.session_id
                        GROUP BY s.id, s.title
                        ORDER BY updated_at DESC
                        LIMIT %s
                    """, (limit,))
                    
                    sessions = []
                    for row in eng.fetchall():
                        sessions.append({
                            'id': row['id'],
                            'title': row['title'],
                            'updated_at': row['updated_at']
                        })
                    
                    return sessions
        except Exception as e:
            logger.error(f"Error listing sessions: {e}")
            return []
    
    def delete_session(self, session_id: str) -> bool:
        """Delete a chat session and all its messages."""
        try:
            with self._get_connection() as conn:
                with conn.cursor() as eng:
                    eng.execute("DELETE FROM chat_sessions WHERE id = %s", (session_id,))
                    conn.commit()
                    return eng.rowcount > 0
        except Exception as e:
            logger.error(f"Error deleting session: {e}")
            return False
    
    def update_session_title(self, session_id: str, title: str):
        """Update session title."""
        try:
            with self._get_connection() as conn:
                with conn.cursor() as eng:
                    eng.execute(
                        "UPDATE chat_sessions SET title = %s WHERE id = %s",
                        (title, session_id)
                    )
                    conn.commit()
        except Exception as e:
            logger.error(f"Error updating session title: {e}")
    

    def is_arabic(self, text: str) -> bool:
        """Simple Arabic detection."""
        arabic_pattern = r'[\u0600-\u06FF]'
        return bool(re.search(arabic_pattern, text))
    # Temporary measure.
    def translate_to_english(self, text: str) -> str:
        """Translate Arabic text to English for RAG matching."""
        try:
            translation_prompt = (
                "You are a professional translator. Your task is to translate Egyptian Arabic text to English accurately. "
                "Focus on preserving the meaning, context, and any HR policy terms or company-specific terminology. "
                "Provide ONLY the English translation without any additional commentary or explanations. "
                "If the text contains HR-related terms, translate them appropriately for search purposes."
            )
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": translation_prompt},
                    {"role": "user", "content": f"Translate this Egyptian Arabic text to English: {text}"}
                ],
                temperature=0.1,
                max_tokens=500
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f"Translation error: {e}")
            return text  # Fallback to original

    def decide_rag_usage(self, query: str) -> Tuple[bool, str, float, str]:
        """Decide whether to use RAG based on similarity score."""
        translated_query = query
        
        # If Arabic query, translate to English for RAG matching
        if self.is_arabic(query):
            translated_query = self.translate_to_english(query)
            logger.info(f"Translated Arabic query: '{query}' to English: '{translated_query}'")
        
        # Get RAG context using translated query for better matching
        rag_context, max_similarity = self.rag_system.get_rag_context(translated_query, self.similarity_threshold)
        use_rag = max_similarity >= self.similarity_threshold
        
        logger.info(f"Query similarity: {max_similarity:.3f}, Threshold: {self.similarity_threshold}, Use RAG: {use_rag}")
        
        return use_rag, rag_context, max_similarity, query  

    
    def generate_response(self, query: str, conversation_history: List[Dict] = None, stream: bool = False) -> Tuple[Union[str, Callable[[], Generator[str, None, None]]], str, float]:
        """Generate response using LLM with optional RAG context"""
        use_rag, rag_context, similarity_score, translated_query = self.decide_rag_usage(query)
        messages = []

        if use_rag and rag_context:
            system_message = f"{self.system_prompt}\n\nContext from company policies:\n{rag_context}"
            logger.info(f" RAG Context being sent to LLM (similarity: {similarity_score:.3f}):\n{rag_context[:200]}...")
        else:
            system_message = self.system_prompt

        messages.append({"role": "system", "content": system_message})

        if conversation_history:
            recent_history = conversation_history[-6:]
            for msg in recent_history:
                if msg['role'] in ['user', 'assistant']:
                    messages.append({
                        "role": msg['role'],
                        "content": msg['content']
                    })

        messages.append({"role": "user", "content": query})

        try:
            logger.info(f"Generating response using model: {self.model} (streaming: {stream})")
            stream_obj = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.1,
                max_tokens=2000,
                stream=True
            )

            if stream:
                def generator():
                    for chunk in stream_obj:
                        if chunk.choices and chunk.choices[0].delta.content:
                            yield chunk.choices[0].delta.content
                return generator, rag_context if use_rag else "", similarity_score
            else:
                response_chunks = []
                for chunk in stream_obj:
                    content = getattr(chunk.choices[0].delta, "content", None)
                    if content:
                        response_chunks.append(content)
                response = "".join(response_chunks)

                if use_rag:
                    logger.info(f"Generated response with RAG context (similarity: {similarity_score:.3f})")
                else:
                    logger.info(f"Generated response without RAG (similarity: {similarity_score:.3f})")

                return response, rag_context if use_rag else "", similarity_score

        except Exception as e:
            logger.error(f"Error generating response: {e}")
            error_response = (
                "I'm sorry, I'm having trouble connecting to the language model. "
                "Please ensure the service is running and try again."
            )
            if stream:
                def error_generator():
                    yield error_response
                return error_generator, "", 0.0
            else:
                return error_response, "", 0.0
    
    def chat(self, session_id: str, user_message: str, stream: bool = False) -> Dict:
        """Handle chat interaction"""
        try:
            # Get history
            conversation_history = self.get_session_messages(session_id)
            
            # Save user message
            self.save_message(session_id, "user", user_message)
            
            # Generate response or generator
            gen_or_resp, rag_context, similarity_score = self.generate_response(
                user_message, conversation_history, stream=stream
            )
            used_rag = similarity_score >= self.similarity_threshold
            
            # If first message, update title
            if len(conversation_history) == 0:
                title = user_message[:50] + ("..." if len(user_message) > 50 else "")
                self.update_session_title(session_id, title)
            
            if stream:
                def saving_generator():
                    chunks = []
                    if callable(gen_or_resp):
                        gen = gen_or_resp()  # Call the generator function
                        for chunk in gen:
                            chunks.append(chunk)
                            yield chunk
                    else:
                        # Handle error case where gen_or_resp is already a string
                        chunks.append(gen_or_resp)
                        yield gen_or_resp
                    full_response = "".join(chunks)
                    self.save_message(session_id, "assistant", full_response, rag_context if used_rag else None, similarity_score)
                
                return {
                    'stream': saving_generator(),
                    'used_rag': used_rag,
                    'similarity_score': similarity_score
                }
            else:
                self.save_message(session_id, "assistant", gen_or_resp, rag_context if used_rag else None, similarity_score)
                
                return {
                    'response': gen_or_resp,
                    'rag_context': rag_context,
                    'similarity_score': similarity_score,
                    'used_rag': used_rag
                }
            
        except Exception as e:
            logger.error(f"Error in chat interaction: {e}")
            return {
                'response': "I apologize, but I encountered an error. Please try again.",
                'rag_context': "",
                'similarity_score': 0.0,
                'used_rag': False
            }
    



if __name__ == "__main__":
    # Test the LLM client
    llm = LLMClient()