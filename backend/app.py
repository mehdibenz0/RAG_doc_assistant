from fastapi import FastAPI
from api.documents import router as documents_router
from api.qa import router as qa_router
from core.logging import setup_logging

setup_logging()

app = FastAPI(title="RAG Document Assistant")

app.include_router(documents_router, prefix="/api")
app.include_router(qa_router, prefix="/api")
