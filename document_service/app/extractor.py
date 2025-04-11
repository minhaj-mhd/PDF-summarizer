import fitz  # PyMuPDF
from io import BytesIO

def extract_text(pdf_bytes: bytes) -> str:
    doc = fitz.open(stream=BytesIO(pdf_bytes), filetype="pdf")
    return "\n".join(page.get_text() for page in doc)
