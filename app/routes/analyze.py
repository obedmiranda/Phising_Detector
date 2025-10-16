from fastapi import APIRouter, UploadFile, File
from app.schemas.email_analysis import EmailAnalysisResponse
import email
from email import policy
from io import BytesIO
from app.chains.phishing_chain import PhishingChain  

router = APIRouter()

@router.post("/analyze", response_model=EmailAnalysisResponse)
async def analyze_email(file: UploadFile = File(...)):
   
    content = await file.read()

    try:
        msg = email.message_from_bytes(content, policy=policy.default)
        sender = msg["From"]
        subject = msg["Subject"]
        body = ""

        # Obtener el cuerpo del mensaje
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body += part.get_content()
        else:
            body = msg.get_content()

    except Exception as e:
        return {
            "classification": "Error",
            "confidence": 0.0,
            "reason": f"Error reading email: {str(e)}",
            "summary": "Could not parse .eml file"
        }
  
    phishing_chain = PhishingChain()

    result = await phishing_chain.analyze_email(
        sender=sender or "Unknown",
        subject=subject or "No Subject",
        email_text=body or ""
    )


    return result
