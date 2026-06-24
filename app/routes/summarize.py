from fastapi import APIRouter, HTTPException

from app.models.schemas import SummaryRequest
from app.services.summarizer import summarize_text
from app.core.logger import logger

router = APIRouter()


@router.post("/summarize")
def summarize(request: SummaryRequest):

    try:

        logger.info("Summarize endpoint called")

        result = summarize_text(request.text)

        return {
            "summary": result
        }

    except Exception as e:

        logger.error(str(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )