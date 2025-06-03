import os

from dotenv import load_dotenv

from frontend.components.classifier import needs_reply_llm
from frontend.components.comment_ops import (
    fetch_unreplied_comments,
    update_comment_reply,
    update_reply_status,
)
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
    print(f"[INFO] Found {len(comments)} unreplied comments.")
    for comment_row in comments:
        comment_id, recipe, name, comment = comment_row

        print(f"[INFO] Checking comment by {name}: {comment}")
        reply_need = needs_reply_llm(comment)
        print(f"[INFO] Reply needed to comment ID {comment_id}->{reply_need}")

        # If no reply is needed

        if not reply_need:
            # Update reply status if no reply is needed
            update_reply_status(comment_id)
            continue

        try:
            # Routing: Wiki or PDF
            source = get_llm_routing_decision(query=comment, recipe=recipe)
            docs = (
                retriever.retrieve(query=comment, recipe=recipe)
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
            reply = get_llm_answer(comment, context, recipe, memory_context)

            update_comment_reply(comment_id, reply)
            print(f"[INFO] Replied to comment ID {comment_id}")

        except Exception as e:
            print(f"[ERROR] Failed to process comment {comment_id}: {e}")


if __name__ == "__main__":
    run_cron()
