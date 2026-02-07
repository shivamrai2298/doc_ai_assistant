from fastapi import FastAPI
from app.api.routes.ingest import router as ingest_router
from app.api.routes.query import router as query_router

app = FastAPI()

app.include_router(ingest_router, prefix="/api")
app.include_router(query_router, prefix="/api")
