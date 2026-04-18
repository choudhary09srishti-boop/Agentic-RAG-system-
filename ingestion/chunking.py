import os

def load_documents(data_dir="data"):
    documents = []
    for file in os.listdir(data_dir):
        if file.endswith(".txt") or file.endswith(".pdf"):
            filepath = os.path.join(data_dir, file)
            with open(filepath, "r", encoding="utf-8") as f:
                documents.append({"filename": file, "content": f.read()})
    return documents

def chunk_text(text, chunk_size=300, overlap=50):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

def chunk_documents(documents, chunk_size=300, overlap=50):
    all_chunks = []
    for doc in documents:
        chunks = chunk_text(doc["content"], chunk_size, overlap)
        for i, chunk in enumerate(chunks):
            all_chunks.append({"source": doc["filename"], "chunk_id": i, "text": chunk})
    return all_chunks
