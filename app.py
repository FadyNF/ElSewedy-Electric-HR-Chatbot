import os
import streamlit as st
from utils.embedding import embed_text
from utils.retrieval import retrieve_chunks_from_db, retrieve_relevant_images
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
    # Show user's message
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        # Get relevant sections
        relevant_chunks = retrieve_chunks_from_db(user_input)
        context_text = build_prompt(user_input, relevant_chunks)

        # Get relevant images
        relevant_images = retrieve_relevant_images(user_input, top_k=2)

        # Get section IDs for optional filtering
        valid_chunk_ids = [chunk["id"] for chunk in relevant_chunks]
        filtered_images = [
            img for img in relevant_images if img["chunk_id"] in valid_chunk_ids
        ]

        # Prepare prompt
        prompt_messages = [
            {
                "role": "system",
                "content": """You are an HR assistant. Be helpful and concise. Also provide context if available. 
                              Mention which PDF or section the information came from when possible.""",
            }
        ]

        # Add previous messages
        for m in st.session_state.chat_history:
            prompt_messages.append({"role": m["role"], "content": m["content"]})

        prompt_messages.append(
            {
                "role": "user",
                "content": f"Use this context to help answer:\n{context_text}\n\n{user_input}",
            }
        )

        # Get assistant response
        assistant_response = ask_openai(prompt_messages)

        st.chat_message("assistant").markdown(assistant_response)
        st.session_state.chat_history.append(
            {"role": "assistant", "content": assistant_response}
        )

        # Show relevant images
        if filtered_images:
            st.markdown("📷 **Relevant Diagram(s):**")
            for img in filtered_images:
                image_path =  'data/'+ img["image_path"]
                if os.path.exists(image_path):
                    st.image(
                        image_path, caption=f"Linked to section ID: {img['chunk_id']}"
                    )
                else:
                    st.warning(f"Image not found: {image_path}")

# Sidebar: Clear chat button
with st.sidebar:
    if st.button("🧹 Clear Chat"):
        st.session_state.chat_history = []
