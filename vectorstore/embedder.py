from langchain.schema import Document
from langchain_cohere import CohereEmbeddings


class Embedder:
    def __init__(self, cohere_api_key):
        self.embedding_model = CohereEmbeddings(
            cohere_api_key=cohere_api_key, model="embed-english-v3.0"
        )

    def embed_documents(self, documents):
        # Extract content from LangChain Documents
        texts = [doc.page_content for doc in documents]
        embeddings = self.embedding_model.embed_documents(texts)

        # Return embeddings with metadata included (if any)
        return [
            {"embedding": embedding, "metadata": doc.metadata}
            for embedding, doc in zip(embeddings, documents)
        ]
