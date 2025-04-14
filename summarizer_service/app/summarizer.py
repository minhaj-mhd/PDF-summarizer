from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.generator import generate_summary,get_summary_text

router = APIRouter()

class TextInput(BaseModel):
    content: str

@router.post("/")
async def summerize(input_data:TextInput):
    try:
        summary = generate_summary(input_data.content)
        return {"summary":summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail = str(e))
@router.get("/{doc_id}")
async def get_summary(doc_id:str):
    try:
        text = get_summary_text(doc_id)
        return {"summary":text}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
        
