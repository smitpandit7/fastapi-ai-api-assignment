from fastapi import APIRouter, HTTPException

from app.models.schemas import TranslationRequest
from app.services.translator import translate_text
from app.core.logger import logger

router = APIRouter(
    tags=["Translation"]
)


@router.post("/translate")
def translate(request: TranslationRequest):

    try:

        logger.info(
            f"Translation API called for {request.target_language}"
        )

        translated_text = translate_text(
            request.text,
            request.target_language
        )

        return {
            "translated_text": translated_text
        }

    except Exception as e:

        logger.error(str(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )