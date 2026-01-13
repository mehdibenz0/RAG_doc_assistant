from fastapi import APIRouter, UploadFile, File
import shutil, os

from services.document_service import DocumentService
from services.embedding_service import EmbeddingService
from services.vector_store_service import VectorStoreService
from services.rag_service import RAGService

router = APIRouter()

document_service = DocumentService()
embedding_service = EmbeddingService()
vector_store_service = VectorStoreService()
rag_service = RAGService()

@router.post("/documents")
async def upload_document(file: UploadFile = File(...)):
    os.makedirs("backend/data", exist_ok=True)
    file_path = f"backend/data/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    docs = document_service.load_and_split(file_path)
    embeddings = embedding_service.create()
    vector_store = vector_store_service.build(docs, embeddings)
    rag_service.initialize(vector_store)

    return {"status": "indexed"}
