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
        self.model = os.getenv("MODEL", "gpt-4o-mini")
        self.similarity_threshold = float(os.getenv("SIMILARITY_THRESHOLD", "0.6"))
        
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
            "You are an HR Assistant for Elsewedy Electric, your primary role is to answer questions based on the provided company policies. When relevant policy context is available, use it to respond and cite the source. If no relevant context is provided for a specific question, state, I don’t have that information in the provided policies. DO NOT USE external knowledge about Elsewedy or other companies not explicitly provided in the context. For general questions unrelated to Elsewedy Electric’s policies, you can respond as a helpful chatbot using your available knowledge and tools, ensuring accurate and concise answers.\n\n"
            
            "LANGUAGE HANDLING:\n"
            "- If spoken to in Arabic (العربية), respond in Arabic\n"
            "- If spoken to in English, respond in English\n"
            "- Search for policy information in both Arabic and English content\n"
            "- When citing sources, use the original policy name as it appears in the document\n"
            "- If a policy name is mentioned in Arabic, search for both Arabic and English versions\n\n"
            
            "EXAMPLES:\n\n"
            
            "English Example 1:\n"
            "Question: What is the dress code for office employees at Elsewedy Electric?\n"
            "Answer: Based on the Dress Code & Personal Appearance Policy, for offices, employees are required to wear formal or semi-formal attire, including suits, jackets, shirts, skirts, and pants typical of formal business attire. All clothing should be neat, without tears, revealing, rips, or holes, and should not be revealing or have offensive stamps or prints. On Thursdays, smart casual wear is accepted, including jeans, polo shirts, t-shirts (no drawings), and sneakers, but slippers, shorts, ripped jeans, and sportswear are not allowed. Females are allowed to wear jewelry, but visible body piercings are not permitted during working hours. Employees must maintain personal hygiene, including neat haircuts, trimmed beards, and proper nail care. (Source: Dress Code & Personal Appearance Policy)\n\n"
            
            "English Example 2:\n"
            "Question: What are the criteria for band promotion at Elsewedy Electric?\n"
            "Answer: According to the Promotion Policy, band promotion is an upward move from one band to another and requires the employee to be a confirmed High Potential (HIPO) as identified through the Talent Review Meeting (TRM) and the Group Talent Assessment Center (TAC). The criteria include: 1. Approved organization structure. 2. Available job at the requested grade. 3. Available budget. 4. The readiness of the nominated employee (confirmed HIPO). 5. Approval of the Sector/BU Head. Additionally, for leadership band jobs, approval from the Group CHRO and Group CEO is required. (Source: Promotion Policy)\n\n"
            
            "Arabic Example 1:\n"
            "السؤال: إيه هي سياسة السلف في الشركة؟\n"
            "الإجابة: بناءً على سياسة سلف العاملين، يحق للموظفين الحصول على سلف وفقاً للشروط والأحكام المحددة في السياسة. يجب تقديم طلب السلفة وفقاً للإجراءات المعتمدة والحصول على الموافقات اللازمة من الإدارة المختصة. (المصدر: سياسة سلف العاملين)\n\n"
            
            "Arabic Example 2:\n"
            "السؤال: اعمل ايه عشان اترقي؟\n"
            "الإجابة: وفقاً لسياسة الترقيات، الترقية في الدرجة الوظيفية تتطلب أن يكون الموظف مؤهل ومحدد كموظف عالي الإمكانات (HIPO) من خلال اجتماع مراجعة المواهب ومركز تقييم المواهب. المعايير تشمل: ١. هيكل تنظيمي معتمد ٢. وظيفة متاحة في الدرجة المطلوبة ٣. ميزانية متاحة ٤. جاهزية الموظف المرشح ٥. موافقة رئيس القطاع/وحدة العمل. (المصدر: سياسة الترقيات)\n\n"
            
            "General Knowledge Example:\n"
            "Question: What is AI?\n"
            "Answer: Artificial Intelligence (AI) is the use of machines to perform tasks that normally require human intelligence—like learning, decision-making, and pattern recognition. For businesses, AI drives efficiency, automates processes, and supports smarter, data-driven decisions.\n\n"
            
            "No Context Example:\n"
            "Question: What is the vacation policy for contractors?\n"
            "Answer: I don't have specific information about vacation policies for contractors in the provided policies. Could you clarify if you're another policy or a different question?\n\n"
            
            "Arabic No Context Example:\n"
            "السؤال: إيه هي سياسة الإجازات للمقاولين؟\n"
            "الإجابة: مش عندي معلومات محددة عن سياسة الإجازات للمقاولين في السياسات المتاحة. ممكن توضح لو بتسأل عن سياسة مختلفة؟"
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
    
    def decide_rag_usage(self, query: str) -> Tuple[bool, str, float, str]:
        """Decide whether to use RAG based on similarity score, with Arabic query translation."""
        translated_query = query  # Default to original
        
        # Detect if query is Arabic
        if self.is_arabic(query):
            # Translate to English for better RAG matching with English policies
            translated_query = self.translate_to_english(query)
            logger.info(f"Translated Arabic query: '{query}' to English: '{translated_query}'")
        
        rag_context, max_similarity = self.rag_system.get_rag_context(translated_query, self.similarity_threshold)
        use_rag = max_similarity >= self.similarity_threshold
        
        logger.info(f"Query similarity: {max_similarity:.3f}, Threshold: {self.similarity_threshold}, Use RAG: {use_rag}")
        
        return use_rag, rag_context, max_similarity, translated_query
    
    def is_arabic(self, text: str) -> bool:
        """Simple Arabic detection."""
        arabic_pattern = r'[\u0600-\u06FF]'
        return bool(re.search(arabic_pattern, text))
    
    def translate_to_english(self, text: str) -> str:
        """Translate text to English using the LLM."""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a translator. Translate the following Egyptian Arabic text to English accurately, preserving HR policy terms."},
                    {"role": "user", "content": text}
                ],
                temperature=0.3,
                max_tokens=1500
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f"Translation error: {e}")
            return text  # Fallback to original
    
    def generate_response(self, query: str, conversation_history: List[Dict] = None, stream: bool = False) -> Tuple[Union[str, Callable[[], Generator[str, None, None]]], str, float]:
        """Generate response using LLM with optional RAG context, optionally streaming."""
        use_rag, rag_context, similarity_score, translated_query = self.decide_rag_usage(query)
        messages = []

        if use_rag and rag_context:
            system_message = f"{self.system_prompt}\n\nContext from company policies:\n{rag_context}"
            logger.info(f"🔍 RAG Context being sent to LLM (similarity: {similarity_score:.3f}):\n{rag_context[:200]}...")
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
                temperature=0.5,
                max_tokens=1500,
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
        """Handle chat interaction with optional streaming."""
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
    
    # Create a test session
    session_id = llm.create_session("Test Session")
    print(f"Created session: {session_id}")
    
    # Test chat
    result = llm.chat(session_id, "What is the dress code policy?")
    print(f"Response: {result['response']}")
    print(f"Used RAG: {result['used_rag']}")
    print(f"Similarity: {result['similarity_score']:.3f}")
    
    # List sessions
    sessions = llm.list_sessions()
    print(f"Sessions: {len(sessions)}")
