import os

from dotenv import load_dotenv

from loaders.pdf_loader import load_and_chunk_pdfs
from utils.config_loader import load_config
from vectorstore.embedder import Embedder
from vectorstore.pinecone_uploader import PineconeUploader


def main():
    # Load configuration
    config = load_config()
    load_dotenv()
    pdf_info_list = config["pdf_paths"]
    cohere_api_key = os.getenv("COHERE_API_KEY")
    pinecone_api_key = os.getenv("PINECONE_API_KEY")
    pinecone_index = config["pinecone"]["index_name"]
    pinecone_dim = config["pinecone"]["dimension"]
    # namespace = pdf_info.get("namespace", "default")

    # Step 1: Load and split PDF
    chunks = load_and_chunk_pdfs(pdf_info_list)

    # Step 2: Embed
    embedder = Embedder(cohere_api_key)
    embedded_docs = embedder.embed_documents(chunks)

    # Step 3: Upsert to Pinecone
    uploader = PineconeUploader(
        api_key=pinecone_api_key,
        index_name=pinecone_index,
        dimension=pinecone_dim,
    )
    uploader.upsert_documents(chunks, [item["embedding"] for item in embedded_docs])


if __name__ == "__main__":
    main()
