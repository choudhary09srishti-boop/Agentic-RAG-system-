from ingestion.embedding import get_embeddings
from ingestion.vector_store import load_vector_store, search

index, chunks = load_vector_store()

def retrieve(query, top_k=3):
    query_embedding = get_embeddings([{"text": query}])[0]
    results = search(query_embedding, index, chunks, top_k=top_k)
    return results