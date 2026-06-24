from pydantic import BaseModel, Field


class SummaryRequest(BaseModel):
    text: str = Field(..., min_length=10)


class TranslationRequest(BaseModel):
    text: str = Field(..., min_length=1)
    target_language: str = Field(..., min_length=2)


class EmailRequest(BaseModel):
    purpose: str = Field(..., min_length=5)
    recipient: str = Field(..., min_length=2)
    tone: str = Field(..., min_length=2)