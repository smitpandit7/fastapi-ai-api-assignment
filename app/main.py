from fastapi import FastAPI

from app.routes.summarize import router as summarize_router
from app.routes.translate import router as translate_router

app = FastAPI(
    title="AI Utility API",
    description="FastAPI application for Summarization, Translation and Email Generation",
    version="1.0.0"
)

app.include_router(summarize_router)
app.include_router(translate_router)

@app.get("/")
def root():
    return {
        "message": "AI Utility API Running Successfully"
    }