from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
import requests
from get_answers import answer_question
router = APIRouter()

class QuestionInput(BaseModel):
    doc_id :str
    question: str


@router.post("/question")
async def question(question : QuestionInput):
    url = f"http://localhost:8001/summarize/{question.doc_id}"
    response = requests.get(url)
    if response.status_code == 200:
        summary = response.json()["summary"]
        answer = answer_question(summary,question.question)
    else:
        raise HTTPException(status_code=400, detail="Incorrece response from summarizer service")
    return answer