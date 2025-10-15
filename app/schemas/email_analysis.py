from pydantic import BaseModel, Field
from typing import Optional, List

class EmailLink(BaseModel):
    url:str
    is_suspicious: bool
    reason: Optional[str]

class EmailMetadata(BaseModel):
     sender: str 
     subject: str 
     received_date: Optional[str]

class EmailAnalysisResponse(BaseModel):
    classification: str = Field(
        ..., example="Phishing", description="Overall classification result"
    )
    confidence: float = Field(
        ..., example=0.92, description="Confidence score from 0 to 1"
    )
    reason: str = Field(
        ..., example="Suspicious link and urgent tone detected"
    )
    summary: Optional[str] = Field(
        None,
        example="Email pretends to be from Microsoft security team requesting urgent login verification.",
    )
    links: Optional[List[EmailLink]] = Field(
        None, description="List of detected links and their risk evaluation"
    )
    metadata: Optional[EmailMetadata] = Field(
        None, description="Basic metadata extracted from the email"
    )

class EmailAnalysisRequest(BaseModel):
    email_text: str = Field(
        ..., description="Raw email text or parsed content for analysis"
    )

    class Config:
        schema_extra = {
            "example": {
                "email_text": "Dear user, your account will be suspended. Please login at https://login.microsoft-secure.com"
            }
        }