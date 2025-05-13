import os

import requests
from dotenv import load_dotenv

from utils.config_loader import load_config

config = load_config()
load_dotenv() 

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = config["groq"].get("model", "llama3-8b-8192")


# Function to build a QA prompt for the LLM
def build_qa_prompt(context: str, question: str) -> str:
    return f"""
You are a helpful AI assistant answering questions about cooking.

Use the following context to answer the user's question.
If the context does not contain enough information, say "I’m not sure based on the current data."

Context:
\"\"\"{context}\"\"\"

Question:
\"{question}\""

Answer in a friendly and concise manner.
""".strip()


# Function to get the LLM's answer
def get_llm_answer(question: str, context: str, memory_context: str = "") -> str:
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    # Create the full prompt to include memory context
    full_prompt = f"""
You are a helpful AI assistant answering cooking questions.

This is the past conversation for reference:
\"\"\"{memory_context}\"\"\"

Use the following context (from documents) to answer the current question:
\"\"\"{context}\"\"\"

Current Question:
\"{question}\""

Respond in a friendly, clear way.
""".strip()

    payload = {
        "model": GROQ_MODEL,
        "messages": [{"role": "user", "content": full_prompt}],
    }

    try:
        # Make a POST request to the Groq API
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            json=payload,
            headers=headers,
        )
        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"].strip()

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request failed: {e}")
        return "Sorry, I couldn't process the request at the moment."
