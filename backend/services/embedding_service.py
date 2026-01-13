from langchain.embeddings import OpenAIEmbeddings
from core.config import settings

class EmbeddingService:

    def create(self):
        return OpenAIEmbeddings(model=settings.EMBEDDING_MODEL)
