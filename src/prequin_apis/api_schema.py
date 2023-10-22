from pydantic import BaseModel, Field


class SentenceInput(BaseModel):
    """
    Json Response Model for API response
    """

    sentence: str = Field(description="Str input")

