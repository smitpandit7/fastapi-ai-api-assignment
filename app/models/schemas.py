from pydantic import BaseModel, Field
from enum import Enum
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


class ToneEnum(str, Enum):
    professional = "professional"
    friendly = "friendly"
    formal = "formal"


class EmailRequest(BaseModel):
    purpose: str = Field(..., min_length=5)
    recipient: str = Field(..., min_length=2)
    tone: ToneEnum