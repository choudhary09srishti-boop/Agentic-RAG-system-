import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.3-70b-versatile"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
VECTOR_DB_PATH = "data/vector_store"
CHUNK_SIZE = 300
CHUNK_OVERLAP = 50
TOP_K = 3