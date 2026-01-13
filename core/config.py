import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "RAG Document Assistant"
    ENV = os.getenv("ENV", "dev")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    EMBEDDING_MODEL = "text-embedding-3-small"
    LLM_MODEL = "gpt-4o-mini"

    CHUNK_SIZE = 600
    CHUNK_OVERLAP = 100

    TOP_K_RETRIEVAL = 4

settings = Settings()
