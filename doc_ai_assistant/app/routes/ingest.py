from fastapi import APIRouter, UploadFile, File
from app.ingestion.pipeline import ingest_document

router = APIRouter()

@router.post("/ingest")
async def ingest(file: UploadFile = File(...)):
    result = ingest_document(file)
    return {"message": result}

