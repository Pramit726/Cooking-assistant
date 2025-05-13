import os

import requests
from dotenv import load_dotenv

from utils.config_loader import load_config

config = load_config()
load_dotenv()
pdf_summary = config["pdf_summary"]  # Load from config instead of hardcoding


# Function to build the routing prompt for the LLM
def build_routing_prompt(query: str, pdf_summary: str) -> str:
    return f"""
You are an intelligent assistant. Based on the following context from a PDF and the user query,
decide whether the answer can be found in the PDF or should be looked up on Wikipedia.

Context from PDF:
\"\"\"{pdf_summary}\"\"\"

User Query:
\"{query}\"

Respond with either 'pdf' if the answer is in the PDF, or 'wikipedia' if it should be looked up on Wikipedia.
""".strip()


# Function to get the LLM's decision on where to route the query
def get_llm_routing_decision(query: str) -> str:
    groq_api_key = os.getenv("GROQ_API_KEY")
    model = config["groq"].get("model", "llama3-8b-8192")

    # Prepare the routing prompt with the user query and PDF summary
    prompt = build_routing_prompt(query, pdf_summary)

    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json",
    }

    # Request to Groq API
    body = {"model": model, "messages": [{"role": "user", "content": prompt}]}

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            json=body,
            headers=headers,
        )
        response.raise_for_status()
        decision = response.json()["choices"][0]["message"]["content"].strip().lower()
        print(f"[DEBUG] LLM routing decision: {decision}")

        # Ensure the decision is either 'pdf' or 'wikipedia'
        if "pdf" in decision:
            return "pdf"
        else:
            return "wikipedia"

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request to Groq API failed: {e}")
        return "wikipedia"  # Default to Wikipedia if there's an error
