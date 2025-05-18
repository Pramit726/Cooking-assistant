import os

from classifier import needs_reply_llm
from comment_ops import fetch_unreplied_comments, update_comment_reply
from dotenv import load_dotenv

from llm.groq_qa import get_llm_answer
from loaders.wiki_loader import get_wiki_chunks
from memory.conversation_memory import ConversationMemory
from retriever.retriever import Retriever
from retriever.router import get_llm_routing_decision
from utils.config_loader import load_config

# Load config and initialize retriever
config = load_config()
load_dotenv()

retriever = Retriever(
    cohere_api_key=os.getenv("COHERE_API_KEY"),
    pinecone_api_key=os.getenv("PINECONE_API_KEY"),
    index_name=config["pinecone"]["index_name"],
)

memory = ConversationMemory(max_memory=5)


def run_cron():
    comments = fetch_unreplied_comments()
    for comment_row in comments:
        comment_id, recipe, name, comment = comment_row

        print(f"🔍 Checking comment by {name}: {comment}")
        if not needs_reply_llm(comment):
            continue

        try:
            # Routing: Wiki or PDF
            source = get_llm_routing_decision(recipe)
            docs = (
                retriever.retrieve(recipe)
                if source == "pdf"
                else get_wiki_chunks(recipe)
            )

            if not docs:
                print("[DEBUG] No context found for recipe:", recipe)
                continue

            context = "\n".join(
                [doc.page_content for doc in docs if doc.page_content.strip()]
            )
            memory_context = memory.get_memory_context()
            reply = get_llm_answer(comment, context, memory_context)

            update_comment_reply(comment_id, reply)
            print(f"[INFO] Replied to comment ID {comment_id}")

        except Exception as e:
            print(f"[ERROR] Failed to process comment {comment_id}: {e}")
