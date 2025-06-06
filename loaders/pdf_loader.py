from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader


def load_and_chunk_pdfs(pdf_info_list, chunk_size=500, chunk_overlap=50):
    all_chunks = []
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )

    # print(f"[INFO]info list{pdf_info_list}")

    for pdf_info in pdf_info_list:
        try:
            pdf_path = pdf_info["path"]
            reader = PdfReader(pdf_path)
            full_text = "\n".join(
                page.extract_text() for page in reader.pages if page.extract_text()
            )

            chunks = splitter.create_documents([full_text])
        except Exception as e:
            print(f"[ERROR] Failed to read {pdf_path}: {e}")

        for doc in chunks:
            doc.metadata.update(
                {
                    "source": "pdf",
                    "filename": pdf_path,
                    "namespace": pdf_info.get("namespace", "default"),
                }
            )

        all_chunks.extend(chunks)


    return all_chunks  # Returns combined List[Document]
