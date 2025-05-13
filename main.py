from llm.groq_qa import get_llm_answer
from memory.conversation_memory import ConversationMemory
from retriever.retriever import Retriever
from retriever.router import get_llm_routing_decision
from utils.config_loader import load_config
from loaders.wiki_loader import get_wiki_chunks

config = load_config()
retriever = Retriever(
    cohere_api_key=config["cohere"]["api_key"],
    pinecone_api_key=config["pinecone"]["api_key"],
    # pinecone_env=config["pinecone"]["environment"],
    index_name=config["pinecone"]["index_name"],
)


def main():
    print("🍳 Welcome to RasoiGuru - Your AI Cooking Assistant!")
    memory = ConversationMemory(max_memory=5)

    while True:
        query = input("\n👤 You: ").strip()

        # Exit condition
        if query.lower() in ["exit", "quit"]:
            print("👋 Goodbye! Happy Cooking!")
            break

        try:
            # Step 1: Decide source (PDF or Wikipedia)
            source = get_llm_routing_decision(query)
            print(f"📚 Using source: {'PDF' if source == 'pdf' else 'Wikipedia'}")

            # Step 2: Retrieve relevant documents based on source
            # docs = get_relevant_documents(query, source)
            if source == "pdf":
                # For PDF, use the retriever to get relevant documents
                docs = retriever.retrieve(query)
                print("📄 Retrieved documents from PDF:")
                # print(type(docs))
                # print(f"🔍 Found \n{docs}")
            else:
                # For Wikipedia, use the wiki_loader to get relevant documents
                docs = get_wiki_chunks(topic=query)
                print("📄 Retrieved documents from wikipedia:")
                # print(type(docs))
                # print(f"🔍 Found \n{docs}")
            

            if not docs:
                print("⚠️ No relevant documents found.")
                continue

            # Concatenate the document content to form the context
            context = "\n".join([doc.page_content for doc in docs])

            # Step 3: Retrieve memory context (if any)
            memory_context = memory.get_memory_context()

            # Step 4: Get the answer from the LLM
            answer = get_llm_answer(query, context, memory_context)

            print(f"🤖 RasoiGuru: {answer}")

            # Add the current interaction to memory
            memory.add_interaction(query, answer)

        except Exception as e:
            print("❌ Error:", e)


# Entry point to the script
if __name__ == "__main__":
    main()
