from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader


def load_and_chunk_pdfs(pdf_paths, chunk_size=500, chunk_overlap=50):
    all_chunks = []
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )

    for pdf_path in pdf_paths:
        reader = PdfReader(pdf_path)
        full_text = "\n".join(
            page.extract_text() for page in reader.pages if page.extract_text()
        )

        chunks = splitter.create_documents([full_text])

        for doc in chunks:
            doc.metadata.update({"source": "pdf", "filename": pdf_path})

        all_chunks.extend(chunks)

    return all_chunks  # Returns combined List[Document]
