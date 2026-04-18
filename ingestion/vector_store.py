import faiss
import numpy as np
import pickle
import os
from config import VECTOR_DB_PATH

def save_vector_store(chunks, embeddings):
    os.makedirs(VECTOR_DB_PATH, exist_ok=True)
    embeddings = np.array(embeddings).astype("float32")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    faiss.write_index(index, f"{VECTOR_DB_PATH}/index.faiss")
    with open(f"{VECTOR_DB_PATH}/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)
    print("Vector store saved.")

def load_vector_store():
    index = faiss.read_index(f"{VECTOR_DB_PATH}/index.faiss")
    with open(f"{VECTOR_DB_PATH}/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)
    return index, chunks

def search(query_embedding, index, chunks, top_k=3):
    query_embedding = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(query_embedding, top_k)
    results = [chunks[i] for i in indices[0]]
    return results
