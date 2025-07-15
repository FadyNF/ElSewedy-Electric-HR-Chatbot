import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def build_prompt(question, chunks):
    context = "\n\n".join([f"[{c['title']}]\n{c['content']}" for c in chunks])
    return f"""You are an HR assistant for ElSewedy Electric Company. Check the answer for the question sent in the context sent with it. 
    If unsure say I don't know.

    Context:
    {context}

    Question:
    {question}

    Answer:"""

def format_messages(messages):
    """
    Ensures each message's content is a list of blocks with the correct type,
    as required by the latest OpenAI Python SDK.
    """
    formatted = []
    for msg in messages:
        content = msg["content"]
        # If already in new format, keep as is
        if isinstance(content, list) and len(content) > 0 and isinstance(content[0], dict) and "type" in content[0]:
            formatted.append(msg)
        else:
            formatted.append({
                "role": msg["role"],
                "content": [{"type": "text", "text": content}]
            })
    return formatted

def ask_openai(messages, model="gpt-3.5-turbo"):
    """
    Accepts a list of messages (role/content dicts), formats them if needed,
    and sends to the OpenAI chat completion API.
    """
    formatted_messages = format_messages(messages)
    response = client.chat.completions.create(
        model=model,
        messages=formatted_messages
    )
    return response.choices[0].message.content