from langchain.vectorstores import FAISS
from typing import List
from langchain.schema import Document

class VectorStoreService:

    def build(self, documents: List[Document], embeddings) -> FAISS:
        return FAISS.from_documents(documents, embeddings)
