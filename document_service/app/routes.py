from fastapi import APIRouter, UploadFile, File, HTTPException
from app.extractor import extract_text
from app.database import save_document

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDFs allowed")

    contents = await file.read()
    text = extract_text(contents)
    doc_id = await save_document(file.filename, text)
    return {"id": str(doc_id), "message": "Document uploaded" , "text": text}
