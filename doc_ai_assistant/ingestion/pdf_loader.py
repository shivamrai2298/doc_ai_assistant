import fitz
from app.ingestion.ocr import ocr_extract

def extract_text(file):
    pdf = fitz.open(stream=file.file.read(), filetype="pdf")
    text = ""

    for page in pdf:
        text += page.get_text()

    if text.strip():
        return text
    else:
        return ocr_extract(file)
