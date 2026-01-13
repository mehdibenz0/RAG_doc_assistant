from pydantic import BaseModel

class QuestionRequest(BaseModel):
    query: str

class AnswerResponse(BaseModel):
    answer: str
