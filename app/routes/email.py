from fastapi import APIRouter, HTTPException

from app.models.schemas import EmailRequest
from app.services.email_generator import generate_email
from app.core.logger import logger

router = APIRouter()


@router.post("/generate-email")
def generate_email_endpoint(
    request: EmailRequest
):

    try:

        logger.info(
            f"Email generation API called for {request.recipient}"
        )

        email = generate_email(
            purpose=request.purpose,
            recipient=request.recipient,
            tone=request.tone
        )

        return {
            "generated_email": email
        }

    except Exception as e:

        logger.error(str(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )