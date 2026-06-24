from pydantic import BaseModel, Field
from typing import Literal


class SummaryRequest(BaseModel):
    text: str = Field(..., min_length=10)



class TranslationRequest(BaseModel):
    text: str

    target_language: Literal[
        "hindi",
        "English",
        "french",
        "german",
        "spanish",
        "marathi"
    ]


class EmailRequest(BaseModel):
    purpose: str = Field(..., min_length=5)
    recipient: str = Field(..., min_length=2)
    tone: str = Field(..., min_length=2)