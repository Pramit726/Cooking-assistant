import wikipedia
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from wikipedia.exceptions import DisambiguationError, PageError

def get_wiki_chunks(topic, chunk_size=500, chunk_overlap=50, max_chunks=5):
    try:
        content = wikipedia.page(topic).content
    except DisambiguationError as e:
        print(f"[WARNING] '{topic}' is ambiguous. Using first suggestion: {e.options[0]}")
        content = wikipedia.page(e.options[0]).content
    except PageError:
        print(f"[ERROR] Page not found for topic: {topic}")
        return []

    # Avoid empty or short content
    if not content.strip():
        print(f"[ERROR] No content found for topic: {topic}")
        return []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.create_documents([content])

    # Add metadata and limit number of chunks
    for doc in chunks:
        doc.metadata.update({"source": "wikipedia", "title": topic})

    limited_chunks = chunks[:max_chunks]
    print(f"[INFO] Returning top {len(limited_chunks)} Wikipedia chunks")

    return limited_chunks  # Returns List[Document]


if __name__ == "__main__":
    docs = get_wiki_chunks(topic="Idli")
    print(docs[0].page_content)
