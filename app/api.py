from fastapi import FastAPI, HTTPException
from llm.groq_qa import get_llm_answer
from memory.conversation_memory import ConversationMemory
from retriever.retriever import Retriever
from retriever.router import get_llm_routing_decision
from utils.config_loader import load_config
from loaders.wiki_loader import get_wiki_chunks
from .schemas import QueryRequest
import os
from dotenv import load_dotenv

# Load config and initialize retriever
config = load_config()
load_dotenv()

retriever = Retriever(
    cohere_api_key=os.getenv("COHERE_API_KEY"),
    pinecone_api_key=os.getenv("PINECONE_API_KEY"),
    index_name=config["pinecone"]["index_name"],
)

# Set up FastAPI app
app = FastAPI(title="RasoiGuru - AI Cooking Assistant")
memory = ConversationMemory(max_memory=5)

# Endpoint
@app.post("/chat")
def chat_with_rasoiguru(request: QueryRequest):
    query = request.query.strip()

    if not query:
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    try:
        # Step 1: Decide source
        source = get_llm_routing_decision(query)
        print(f"📚 Using source: {'PDF' if source == 'pdf' else 'Wikipedia'}")

        # Step 2: Retrieve documents
        if source == "pdf":
            docs = retriever.retrieve(query)
        else:
            docs = get_wiki_chunks(topic=query)

        if not docs:
            return {"response": "⚠️ No relevant documents found."}

        # Step 3: Concatenate content
        context = "\n".join([doc.page_content for doc in docs if doc.page_content.strip()])

        # Step 4: Memory context
        memory_context = memory.get_memory_context()

        # Step 5: LLM response
        answer = get_llm_answer(query, context, memory_context)

        # Step 6: Add to memory
        memory.add_interaction(query, answer)

        return {"response": answer}

    except Exception as e:
        print(f"[ERROR] {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)