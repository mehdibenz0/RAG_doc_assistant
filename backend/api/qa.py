from fastapi import APIRouter
from models.schemas import QuestionRequest, AnswerResponse
from services.rag_service import rag_service
from core.exceptions import DocumentNotIndexedError

router = APIRouter()

@router.post("/qa", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    try:
        answer = rag_service.ask(request.query)
        return {"answer": answer}
    except DocumentNotIndexedError as e:
        return {"answer": str(e)}
