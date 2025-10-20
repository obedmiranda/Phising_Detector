🧠 Phishing Detector  
AI-powered email phishing detection system built with FastAPI, LangChain, and OpenAI.

This project analyzes .eml email files to detect and classify potential phishing attempts using natural language understanding and structured reasoning.  
It provides a simple and elegant web interface inspired by ChatGPT’s minimal design.

---

🚀 Features

- Upload .eml email files directly from the UI.  
- Parse and extract metadata (sender, subject, body) from email messages.  
- Analyze the message content using LangChain + OpenAI GPT-4.  
- Classify emails as Phishing, Suspicious, or Safe.  
- Return structured results including:
  - Classification
  - Confidence score
  - Reasoning summary
  - Email metadata and detected links  

---

🧩 Project Structure

Phishing_Detector/
│
├── app/
│   ├── main.py                  # FastAPI entrypoint
│   ├── routes/
│   │   └── analyze.py           # /api/analyze endpoint
│   ├── schemas/
│   │   └── email_analysis.py    # Pydantic models
│   ├── chains/
│   │   └── phishing_chain.py    # LangChain-based analyzer
│   ├── services/
│   │   ├── email_parser.py      # Parses .eml files
│   │   └── domain_checker.py    # Domain validation (future use)
│   └── utils/
│       └── formatter.py         # Utility functions
│
├── templates/
│   └── index.html               # Frontend (HTML + JS + Fetch API)
│
├── static/
│   └── style.css                # Custom UI styling
│
├── .env                         # Environment variables (API keys)
├── requirements.txt             # Python dependencies
└── README.txt

---

🧠 How It Works

1. The user uploads an .eml file through the web interface.  
2. The backend extracts metadata and email content using Python’s `email` library.  
3. The text is passed to a LangChain chain powered by OpenAI GPT-4.  
4. The model analyzes the email and returns a structured JSON response.  
5. The UI displays the result beautifully in a ChatGPT-style response box.

---

🧱 Stack

- Backend: FastAPI  
- Frontend: HTML + Vanilla JS + Fetch API  
- AI Layer: LangChain + OpenAI GPT-4  
- Schema Validation: Pydantic  
- Environment Management: python-dotenv  

---

⚙️ Setup

1. Clone the repository:
   git clone https://github.com/obedmiranda/Phishing_Detector.git
   cd Phishing_Detector

2. Create a virtual environment and install dependencies:
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. Create a .env file and add your OpenAI API key:
   OPENAI_API_KEY=sk-...

4. Run the development server:
   fastapi dev app/main.py

5. Open your browser at:
   http://127.0.0.1:8000

---

🧩 Future Enhancements

- Add RAG (Retrieval-Augmented Generation) for contextual detection  
- Include link domain reputation scoring  
- Add dataset indexing with FAISS or Chroma  
- Build an analytics dashboard for classification trends  
- Deploy on Docker + AWS Lightsail  

---

📚 References

- LangChain Documentation: https://python.langchain.com  
- FastAPI Docs: https://fastapi.tiangolo.com  
- OpenAI API Reference: https://platform.openai.com/docs  

---

## Upcoming: RAG Integration
- Add document loaders (PDF, email, CSV)
- Embed known phishing and safe examples
- Build a retrieval layer to give context to the LLM
🧑‍💻 Author

Obed Miranda Picado  

