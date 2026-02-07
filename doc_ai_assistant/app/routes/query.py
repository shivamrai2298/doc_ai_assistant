from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.qa_chain import answer_question

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/query")
def query_doc(request: QueryRequest):
    answer = answer_question(request.question)
    return {"answer": answer}

