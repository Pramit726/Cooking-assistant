from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader


def load_and_chunk_pdf(pdf_path, chunk_size=500, chunk_overlap=50):
    reader = PdfReader(pdf_path)
    full_text = "\n".join(
        page.extract_text() for page in reader.pages if page.extract_text()
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )

    chunks = splitter.create_documents([full_text])

    # Add metadata to each Document
    for doc in chunks:
        doc.metadata.update({"source": "pdf", "filename": pdf_path})

    return chunks  # Returns List[Document]
