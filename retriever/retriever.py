from langchain.schema import Document
from langchain_cohere import CohereEmbeddings
from pinecone import Pinecone, ServerlessSpec


class Retriever:
    def __init__(self, cohere_api_key, pinecone_api_key, index_name):
        self.embedder = CohereEmbeddings(
            cohere_api_key=cohere_api_key, model="embed-english-v3.0"
        )
        pinecone = Pinecone(api_key=pinecone_api_key)
        self.index = pinecone.Index(index_name)

    def retrieve(self, query, top_k=5):
        # Step 1: Embed the query using the same embedder
        query_embedding = self.embedder.embed_query(query)

        # Step 2: Query Pinecone for the most similar vectors
        results = self.index.query(
            vector=query_embedding, top_k=top_k, include_metadata=True
        )
        print(f"[INFO] Retrieved {len(results['matches'])} matches from Pinecone")
        print(f"[INFO] Retrieved matches: {results['matches']}")

        # Step 3: Format the results into Documents
        retrieved_chunks = []
        for match in results["matches"]:
            doc = Document(
                page_content=match["metadata"].get("text", ""),
                metadata=match["metadata"],
            )
            retrieved_chunks.append(doc)

        return retrieved_chunks
