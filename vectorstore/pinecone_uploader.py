import uuid

from langchain.schema import Document
from pinecone import Pinecone, ServerlessSpec


class PineconeUploader:
    def __init__(self, api_key, index_name, dimension):
        pinecone = Pinecone(api_key=api_key)

        # Check if index exists, if not create it
        if index_name not in pinecone.list_indexes():
            pinecone.create_index(
                index_name,
                dimension=dimension,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )

        self.index = pinecone.Index(index_name)
        # self.namespace = namespace

    def upsert_documents(self, documents, embeddings):
        vectors = []
        for doc, embedding in zip(documents, embeddings):
            vector_id = str(uuid.uuid4())

            # Extract metadata and include page content
            metadata = dict(doc.metadata)  # Make a copy to avoid side-effects
            metadata["text"] = doc.page_content  # Add page content explicitly

            vectors.append({"id": vector_id, "values": embedding, "metadata": metadata})

        for vector in vectors:
            namespace = vector.get("metadata", {}).get("namespace", "default")
            self.index.upsert(vectors=[vector], namespace=namespace)

        print(f"[INFO] Upserted {len(vectors)} documents to Pinecone")
