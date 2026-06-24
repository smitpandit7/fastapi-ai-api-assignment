from fastapi import FastAPI

from app.routes.summarize import router as summarize_router
from app.routes.translate import router as translate_router
from app.routes.email import router as email_router

app = FastAPI(
    title="AI Utility API",
    description="""
    REST API built using FastAPI that provides:

    • Text Summarization
    • Language Translation
    • AI Email Generation

    Developed as part of the IR Infotech AI/ML Intern Assignment.
    """,
    version="1.0.0",
)
app.include_router(summarize_router)
app.include_router(translate_router)
app.include_router(email_router)

@app.get("/")
def root():
    return {
        "message": "AI Utility API Running Successfully"
    }