import streamlit as st
import streamlit.components.v1 as components
import os
import logging
import html
from datetime import datetime
from dotenv import load_dotenv
from llm_client import LLMClient

# Load environment variables
load_dotenv("config.env")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def is_arabic_text(text):
    """Check if text contains Arabic characters."""
    import re
    arabic_pattern = re.compile(r'[\u0600-\u06FF]')
    return bool(arabic_pattern.search(text))

def get_message_style(text):
    """Get inline style for message based on language."""
    if is_arabic_text(text):
        return 'direction: rtl; text-align: right; font-family: "Segoe UI", "Arial Unicode MS", "Tahoma", Arial, sans-serif; unicode-bidi: bidi-override;'
    else:
        return 'direction: ltr; text-align: left;'

def render_markdown_safely(content: str) -> str:
    """Render markdown safely while preserving Arabic text formatting."""
    import re
    
    # First, escape HTML to prevent XSS
    content = html.escape(content)
    
    # Handle Arabic text better - preserve Arabic punctuation and formatting
    # Bold text: **text** -> <strong>text</strong> (handle Arabic commas properly)
    # Use non-greedy matching and handle Arabic punctuation
    content = re.sub(r'\*\*([^*]+?)\*\*', r'<strong>\1</strong>', content)
    
    # Italic text: *text* -> <em>text</em>
    content = re.sub(r'\*([^*]+?)\*', r'<em>\1</em>', content)
    
    # Numbered lists: 1. text -> <li>text</li>
    content = re.sub(r'^\d+\.\s+(.*?)$', r'<li>\1</li>', content, flags=re.MULTILINE)
    
    # Bullet points: - text or • text -> <li>text</li>
    content = re.sub(r'^[-•]\s+(.*?)$', r'<li>\1</li>', content, flags=re.MULTILINE)
    
    # Handle Arabic bullet points (Arabic bullet: •)
    content = re.sub(r'^•\s+(.*?)$', r'<li>\1</li>', content, flags=re.MULTILINE)
    
    # Wrap consecutive <li> elements in <ol> or <ul>
    lines = content.split('\n')
    result_lines = []
    in_list = False
    list_type = None
    
    for line in lines:
        if line.strip().startswith('<li>'):
            if not in_list:
                # Determine list type based on first item
                if re.match(r'^\d+\.', line.strip()):
                    list_type = 'ol'
                else:
                    list_type = 'ul'
                result_lines.append(f'<{list_type}>')
                in_list = True
            result_lines.append(line)
        else:
            if in_list:
                result_lines.append(f'</{list_type}>')
                in_list = False
            result_lines.append(line)
    
    if in_list:
        result_lines.append(f'</{list_type}>')
    
    return '\n'.join(result_lines)

def display_message(role: str, content: str, msg_id: str = None):
    """Display a chat message with proper styling and markdown support."""
    class_name = "user-message" if role == "user" else "assistant-message"
    msg_id = msg_id or f"msg-{role}"
    style = get_message_style(content)
    
    # Render markdown safely
    rendered_content = render_markdown_safely(content)
    
    return f'<div class="{class_name}" id="{msg_id}" style="{style}">{rendered_content}</div>'

def handle_streaming_response(llm_client, session_id: str, prompt: str, message_placeholder):
    """Handle streaming response with real-time updates."""
    result = llm_client.chat(session_id, prompt)
    full_response = ""
    response_id = f"streaming-{len(st.session_state.messages)}"
    
    for chunk in result['stream']:
        full_response += chunk
        message_placeholder.markdown(
            display_message("assistant", full_response + "▌", response_id), 
            unsafe_allow_html=True
        )
    
    # Final message without cursor
    message_placeholder.markdown(
        display_message("assistant", full_response, f"{response_id}-final"), 
        unsafe_allow_html=True
    )
    
    # Log RAG usage
    if result['used_rag']:
        logger.info(f"RAG used with similarity: {result['similarity_score']:.3f}")
    
    return full_response, result

def inject_arabic_formatting_script():
    """Inject optimized JavaScript for Arabic text formatting."""
    script = """
    <script>
    function isArabic(text) {
        const arabicRegex = /[\u0600-\u06FF]/;
        return arabicRegex.test(text);
    }

    function formatChatMessage(messageElement, text) {
        if (isArabic(text)) {
            messageElement.classList.add("arabic-text");
            messageElement.setAttribute("dir", "rtl");
            messageElement.setAttribute("lang", "ar");
            messageElement.style.direction = "rtl";
            messageElement.style.textAlign = "right";
            messageElement.style.unicodeBidi = "bidi-override";
        } else {
            messageElement.classList.remove("arabic-text");
            messageElement.setAttribute("dir", "ltr");
            messageElement.setAttribute("lang", "en");
            messageElement.style.direction = "ltr";
            messageElement.style.textAlign = "left";
            messageElement.style.unicodeBidi = "normal";
        }
    }
    
    function formatAllMessages() {
        // Target Streamlit chat message containers
        document.querySelectorAll('[data-testid="chatMessage"] .user-message, [data-testid="chatMessage"] .assistant-message').forEach(el => {
            formatChatMessage(el, el.textContent || el.innerText);
        });
        
        // Also target direct message containers
        document.querySelectorAll('.user-message, .assistant-message').forEach(el => {
            formatChatMessage(el, el.textContent || el.innerText);
        });
    }
    
    // Initial formatting
    formatAllMessages();
    
    // Observer for new messages
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.type === 'childList') {
                mutation.addedNodes.forEach(function(node) {
                    if (node.nodeType === Node.ELEMENT_NODE) {
                        // Check for Streamlit chat message containers
                        const streamlitMessages = node.querySelectorAll('[data-testid="chatMessage"] .user-message, [data-testid="chatMessage"] .assistant-message');
                        streamlitMessages.forEach(function(message) {
                            formatChatMessage(message, message.textContent || message.innerText);
                        });
                        
                        // Check for direct message containers
                        const directMessages = node.querySelectorAll('.user-message, .assistant-message');
                        directMessages.forEach(function(message) {
                            formatChatMessage(message, message.textContent || message.innerText);
                        });
                    }
                });
            }
        });
    });    
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
    
    // More frequent fallback for Streamlit's dynamic rendering
    setInterval(formatAllMessages, 1000);
    </script>
    """
    components.html(script, height=0)

def setup_logo():
    """Setup logo file for the application."""
    return "logo.png" if os.path.exists("logo.png") else None

# Initialize components
@st.cache_resource
def get_llm_client():
    """Initialize and cache LLM client."""
    return LLMClient()



def initialize_session_state():
    """Initialize session state variables."""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'current_session_id' not in st.session_state:
        st.session_state.current_session_id = None

    if "page" not in st.session_state:
        st.session_state.page = "home"
    if "chat_input_key" not in st.session_state:
        st.session_state.chat_input_key = 0
    if "faq_prompt" not in st.session_state:
        st.session_state.faq_prompt = None

def create_new_session():
    """Create a new chat session."""
    llm_client = get_llm_client()
    session_id = llm_client.create_session()
    st.session_state.current_session_id = session_id
    st.session_state.messages = []
    st.session_state.chat_input_key += 1
    logger.info(f"Created new session: {session_id}")
    return session_id

def load_session_messages(session_id: str):
    """Load messages for a session."""
    llm_client = get_llm_client()
    messages = llm_client.get_session_messages(session_id)
    
    # Convert to streamlit format
    st_messages = []
    for msg in messages:
        st_messages.append({
            "role": msg["role"],
            "content": msg["content"]
        })
    
    st.session_state.messages = st_messages
    st.session_state.current_session_id = session_id

def home_page():
    """Homepage with ElSewedy Electric branding."""
    logo_path = setup_logo()
    
    st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
    }
    
    /* Hide streamlit elements */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display: none;}
    header[data-testid="stHeader"] {display: none;}
    .stAppHeader {display: none;}
    
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        text-align: center;
        padding: 60px 20px 40px;
    }
    
    .logo-container {
        margin-bottom: 30px;
    }
    
    .company-title {
        color: #c0392b;
        font-size: 2.8rem;
        font-weight: bold;
        margin: 20px 0 15px 0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .subtitle {
        font-size: 1.6rem;
        color: #555;
        margin-bottom: 20px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .welcome-text {
        font-size: 1.2rem;
        color: #444;
        margin: 20px 0 30px 0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .footer-text {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        color: #999;
        font-size: 0.9rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .stButton > button {
        background-color: #c0392b !important;
        color: white !important;
        border: none !important;
        padding: 15px 30px !important;
        font-size: 1.2rem !important;
        border-radius: 8px !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        transition: background-color 0.3s ease !important;
    }
    
    .stButton > button:hover {
        background-color: #a93226 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create centered layout
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Logo
        if logo_path:
            st.image(logo_path, width=300)
        else:
            st.markdown("**ElSewedy Electric Logo**")
        
        # Company title and subtitle
        st.markdown('<h1 class="company-title">ELSEWEDY ELECTRIC</h1>', unsafe_allow_html=True)
        st.markdown('<h2 class="subtitle">ASK HR!</h2>', unsafe_allow_html=True)
        st.markdown('<div class="welcome-text">Welcome to HR Support. How can we help you today?</div>', unsafe_allow_html=True)
        
        # Start Chat button
        if st.button("Start Chat", key="start_chat"):
            # Removed: create_new_session()
            st.session_state.page = "chat"
            st.rerun()
    
    # Footer
    st.markdown('<div class="footer-text">&copy; 2025 ELSEWEDY ELECTRIC – All rights reserved.</div>', unsafe_allow_html=True)

def chat_page():
    """Chat page with full UI functionality."""
    logo_path = setup_logo()
    llm_client = get_llm_client()
    
    # Inject Arabic formatting script
    inject_arabic_formatting_script()
    
    # Optimized message styles with enhanced Arabic alignment
    st.markdown("""
    <style>
    .user-message, .assistant-message {
        border-radius: 8px;
        padding: 15px 20px;
        line-height: 1.4;
        font-size: 1rem;
        word-wrap: break-word;
        overflow-wrap: break-word;
        white-space: normal;
        max-width: 100%;
        box-sizing: border-box;
        display: block;
        width: 100%;
        margin: 0;
    }
    
    .user-message {
        background-color: #c0392b;
        color: #fff;
    }
    
    .assistant-message {
        background-color: #f8f9fa;
        color: #222;
        border: 1px solid #e0e0e0;
    }
    
    /* Arabic text styling - Enhanced */
    .arabic-text {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Segoe UI', 'Arial Unicode MS', 'Tahoma', Arial, sans-serif !important;
        unicode-bidi: bidi-override !important;
    }
    
    .arabic-text * {
        direction: rtl !important;
        text-align: right !important;
        unicode-bidi: embed !important;
    }
    
    /* Enhanced RTL and LTR styling */
    [dir="rtl"], [lang="ar"] {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Segoe UI', 'Arial Unicode MS', 'Tahoma', Arial, sans-serif !important;
        unicode-bidi: bidi-override !important;
    }
    
    [dir="ltr"], [lang="en"] {
        direction: ltr !important;
        text-align: left !important;
        unicode-bidi: normal !important;
    }
    
    /* Force RTL for Arabic text in Streamlit containers */
    [data-testid="chatMessage"] .arabic-text,
    [data-testid="chatMessage"] [dir="rtl"],
    [data-testid="chatMessage"] [lang="ar"] {
        direction: rtl !important;
        text-align: right !important;
        unicode-bidi: bidi-override !important;
    }
    
    /* Force LTR for English text in Streamlit containers */
    [data-testid="chatMessage"] [dir="ltr"],
    [data-testid="chatMessage"] [lang="en"] {
        direction: ltr !important;
        text-align: left !important;
        unicode-bidi: normal !important;
    }
    
    /* Remove extra spacing in chat messages */
    .user-message p, .assistant-message p {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    .user-message br, .assistant-message br {
        display: none !important;
    }
    
    /* Ensure proper text flow without extra breaks */
    .user-message, .assistant-message {
        white-space: normal !important;
        line-height: 1.4 !important;
    }
    
    /* Markdown element styling */
    .user-message strong, .assistant-message strong {
        font-weight: bold !important;
    }
    
    .user-message em, .assistant-message em {
        font-style: italic !important;
    }
    
    .user-message ul, .assistant-message ul,
    .user-message ol, .assistant-message ol {
        margin: 8px 0 !important;
        padding-left: 20px !important;
        padding-right: 20px !important;
    }
    
    .user-message li, .assistant-message li {
        margin: 4px 0 !important;
        line-height: 1.3 !important;
    }
    
    /* Arabic-specific markdown styling */
    .arabic-text strong, [dir="rtl"] strong, [lang="ar"] strong {
        font-weight: bold !important;
        unicode-bidi: embed !important;
    }
    
    .arabic-text ul, .arabic-text ol,
    [dir="rtl"] ul, [dir="rtl"] ol,
    [lang="ar"] ul, [lang="ar"] ol {
        text-align: right !important;
        direction: rtl !important;
    }
    
    .arabic-text li, [dir="rtl"] li, [lang="ar"] li {
        text-align: right !important;
        direction: rtl !important;
        unicode-bidi: embed !important;
    }
    
    /* Chat container optimization */
    [data-testid="chatMessage"] {
        max-width: 100% !important;
        overflow: visible !important;
    }
    
    .chat-header {
        background-color: #fff;
        padding: 5px 2px;
        border-bottom: 1px solid #e0e0e0;
        min-height: 60px;
        display: flex;
        align-items: center;
    }
    
    div.block-container {
        padding-top: 0rem !important;
    }
    
    .chat-header h2 {
        color: #c0392b;
        margin: 0;
        font-size: 3.5rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        if logo_path:
            st.image(logo_path, width=200)
        else:
            st.markdown('<div style="width: 60px; height: 60px; background-color: #c0392b; color: white; display: flex; align-items: center; justify-content: center; border-radius: 4px; font-weight: bold;">LOGO</div>', unsafe_allow_html=True)
        
      
        
        # Optimized sidebar styles
        st.markdown("""
        <style>
        /* Sidebar button base styles */
        div[data-testid="stSidebar"] .stButton > button {
            border-radius: 0px !important;
            margin: 0px !important;
            border: 1px solid transparent !important;
            width: 100% !important;
            text-align: left !important;
            box-shadow: none !important;
            transform: none !important;
            padding: 8px 12px !important;
            font-size: 14px !important;
            justify-content: flex-start !important;
        }
        
        /* Button variants */
        div[data-testid="stSidebar"] button[kind="primary"] {
            background-color: #c0392b !important;
            color: white !important;
        }
        div[data-testid="stSidebar"] button[kind="primary"]:hover {
            background-color: #a93226 !important;
        }
        div[data-testid="stSidebar"] button[kind="secondary"] {
            background-color: transparent !important;
            color: #333 !important;
        }
        div[data-testid="stSidebar"] button[kind="secondary"]:hover {
            background-color: #e9ecef !important;
        }
        
        /* Remove all spacing */
        div[data-testid="stSidebar"] .stButton,
        div[data-testid="stSidebar"] .row-widget.stHorizontal,
        div[data-testid="stSidebar"] [data-testid="column"],
        div[data-testid="stSidebar"] div[data-testid="stHorizontalBlock"],
        div[data-testid="stSidebar"] div[data-testid="stHorizontalBlock"] > div,
        div[data-testid="stSidebar"] .streamlit-expanderContent,
        div[data-testid="stSidebar"] .streamlit-expanderContent > div,
        div[data-testid="stSidebar"] .streamlit-expanderContent .element-container {
            margin: 0px !important;
            padding: 0px !important;
            gap: 0px !important;
        }
        
        /* Seamless expander buttons */
        div[data-testid="stSidebar"] .streamlit-expanderContent button {
            margin: -1px 0 !important;
            border-radius: 0 !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        if st.button("New Chat", type="primary", use_container_width=True):

            
            st.session_state.messages = []
            st.session_state.current_session_id = None
            st.session_state.chat_input_key += 1
            st.rerun()
        
        if st.button("Back to Home", type="secondary", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()
        
        st.markdown("<hr>", unsafe_allow_html=True)
        
        # Frequently Asked Questions expander
        with st.expander("Frequently Asked Questions", expanded=False):
            faqs = [
                "What is the company dress code?",
                "Am I allowed to wear casual clothes?",
                "What are the dress code violations?",
                "Explain the recruitment process on Taleo."
            ]
            for i, faq in enumerate(faqs):
                if st.button(faq, key=f"faq_{i}", use_container_width=True):
                    if not st.session_state.current_session_id:
                        create_new_session()
                    
                    # Set the FAQ as the current prompt for streaming
                    st.session_state.faq_prompt = faq
                    st.rerun()

        # Chat History expander
        with st.expander("Chat History", expanded=False):
            sessions = llm_client.list_sessions()
            if not sessions:
                st.write("No chat history yet")
            else:
                sorted_sessions = sorted(sessions, key=lambda x: x['updated_at'], reverse=True)
                for i, session in enumerate(sorted_sessions):
                    session_id = session['id']
                    title = session['title']
                    truncated_title = (title[:45] + '...') if len(title) > 45 else title
                    is_current = session_id == st.session_state.current_session_id
                    
                    if is_current:
                        st.button(f"{truncated_title} (Current)", key=f"current_{session_id}", disabled=True, type="primary", use_container_width=True)
                    else:
                        if st.button(truncated_title, key=f"select_{session_id}", type="secondary", use_container_width=True):
                            load_session_messages(session_id)
                            st.rerun()
    # Main chat area
    st.markdown('<div class="chat-header"><h2>ASK HR!</h2></div>', unsafe_allow_html=True)
    # Display messages with proper formatting
    if not st.session_state.messages:
        with st.chat_message("assistant"):
            welcome_msg = 'Welcome to HR Support! I can answer questions about company policies, dress code, and HR-related matters. How can I assist you today?'
            st.markdown(display_message("assistant", welcome_msg, "welcome-msg"), unsafe_allow_html=True)
            
    for i, message in enumerate(st.session_state.messages):
        with st.chat_message(message["role"]):
            st.markdown(display_message(message["role"], message["content"], f"msg-{i}-{message['role']}"), unsafe_allow_html=True)
    
    # Handle FAQ prompt with streaming
    if hasattr(st.session_state, 'faq_prompt') and st.session_state.faq_prompt:
        prompt = st.session_state.faq_prompt
        st.session_state.faq_prompt = None  # Clear the FAQ prompt
        
        if not st.session_state.current_session_id:
            create_new_session()
            
        # Display user message
        with st.chat_message("user"):
            st.markdown(display_message("user", prompt), unsafe_allow_html=True)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display streaming assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            with st.spinner("Thinking..."):
                full_response, _ = handle_streaming_response(llm_client, st.session_state.current_session_id, prompt, message_placeholder)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})
        st.rerun()

    # Chat input
    if prompt := st.chat_input("Type your HR question here...", key=f"chat_input_{st.session_state.chat_input_key}"):
        if not st.session_state.current_session_id:
            create_new_session()
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(display_message("user", prompt), unsafe_allow_html=True)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display streaming assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            with st.spinner("Thinking..."):
                full_response, _ = handle_streaming_response(llm_client, st.session_state.current_session_id, prompt, message_placeholder)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})
        st.rerun()
def main():
    """Main application function."""
    st.set_page_config(
        page_title="HR Support – ELSEWEDY ELECTRIC",
        page_icon="🏢",
        layout="wide",
        initial_sidebar_state="expanded"  
    )    
    # Setup logo and initialize session state
    setup_logo()
    initialize_session_state()    
    # Route to appropriate page
    if st.session_state.page == "chat":
        chat_page()
    else:
        home_page()
if __name__ == "__main__":
    main()