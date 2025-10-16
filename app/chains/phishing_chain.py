import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain.chains import LLMChain
from app.schemas.email_analysis import EmailAnalysisResponse

load_dotenv()


class PhishingChain:
    def __init__(self):
        self.model = ChatOpenAI(
            model="gpt-4",
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0.1
        )
        self.parser = PydanticOutputParser(pydantic_object=EmailAnalysisResponse)


        self.prompt = ChatPromptTemplate.from_template("""
            You are an AI security analyst specializing in phishing detection.

            Your task is to analyze the following email and classify it as one of:
            - **Phishing** — clearly malicious or deceptive intent.
            - **Suspicious** — potentially unsafe or containing warning signs.
            - **Safe** — appears legitimate and harmless.

            Base your analysis on the provided sender, subject, and body content.
            Then, explain your reasoning briefly and clearly.

            Return your answer in this JSON format:
            {{
            "classification": "<Phishing | Suspicious | Safe>",
            "confidence": <number between 0 and 1>,
            "reason": "<short explanation>",
            "summary": "<one-sentence summary of the email>"
            }}

            Email details:
            Sender: {sender}
            Subject: {subject}
            Body:
            {email_text}
        """)


    
    async def analyze_email(self, sender: str, subject: str, email_text: str):
            
            format_instructions = self.parser.get_format_instructions()

            chain = self.prompt | self.model | self.parser

            result = await chain.ainvoke({
                "sender": sender,
                "subject": subject,
                "email_text": email_text,
                "format_instructions": format_instructions
            })

            return result