import streamlit as st
from utils.embedding import embed_text
from utils.retrieval import retrieve_chunks_from_db
from utils.llm import build_prompt, ask_openai

st.set_page_config(page_title="HR Chatbot", page_icon="🏢")
st.title("🏢 ElSewedy Electric HR Chatbot")

# Session-based chat memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show previous messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input from user
user_input = st.chat_input("Ask a question about company policy...")

if user_input:
    # Show user's message immediately
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Retrieve relevant chunks
    with st.spinner("Thinking..."):
        relevant_chunks = retrieve_chunks_from_db(user_input)
        context_text = build_prompt(user_input, relevant_chunks)

        prompt_messages = [
            {
                "role": "system",
                "content": """You are an HR assistant.
                Be helpful and concise.
                Also provide context if there is.
                Add refernces from the PDF, which pdf and which section is the data
                from if you know.""",
            }
        ]

        # Convert chat history
        for m in st.session_state.chat_history:
            prompt_messages.append({"role": m["role"], "content": m["content"]})

        # Append current user question with retrieved context
        prompt_messages.append(
            {
                "role": "user",
                "content": f"Use this context to help answer:\n{context_text}\n\n{user_input}",
            }
        )

        # Get response from OpenAI (formatting is handled inside ask_openai)
        assistant_response = ask_openai(prompt_messages)

        # Show assistant's message
        st.chat_message("assistant").markdown(assistant_response)
        st.session_state.chat_history.append(
            {"role": "assistant", "content": assistant_response}
        )

# Sidebar: Clear chat button
with st.sidebar:
    if st.button("🧹 Clear Chat"):
        st.session_state.chat_history = []
