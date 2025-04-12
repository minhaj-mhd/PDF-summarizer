from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.generator import generate_summary

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
