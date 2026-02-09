from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Doc AI Assistant"
    ENV: str = "dev"

    FAISS_INDEX_PATH: str = "data/index.faiss"
    TEXT_STORE_PATH: str = "data/texts.pkl"

    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

settings = Settings()

