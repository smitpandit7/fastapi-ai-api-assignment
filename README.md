# AI Utility API

A REST API application built using FastAPI that provides AI-powered text summarization, language translation, and email generation capabilities.

## Demo Video

A complete walkthrough of the project, architecture, API testing, validation, logging, and documentation can be viewed here:

https://drive.google.com/file/d/17hDMZW7fO9t46KCK_odc2ZnDpsQa1OeL/view?usp=sharing

## Features

* Text Summarization using Groq LLM
* Language Translation using Deep Translator
* AI-powered Email Generation using Groq LLM
* Request Validation with Pydantic
* Exception Handling
* Logging Support
* Environment Variable Management
* Interactive API Documentation with Swagger UI

---

## Tech Stack

* Python
* FastAPI
* Groq API
* Deep Translator
* Pydantic
* Uvicorn
* Python Dotenv

---

## Project Structure

```text
fastapi-ai-api-assignment/
│
├── app/
│   ├── main.py
│   │
│   ├── routes/
│   │   ├── summarize.py
│   │   ├── translate.py
│   │   └── email.py
│   │
│   ├── services/
│   │   ├── summarizer.py
│   │   ├── translator.py
│   │   └── email_generator.py
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── logger.py
│   │   └── exception_handler.py
│
├── logs/
│   └── app.log
│
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/smitpandit7/fastapi-ai-api-assignment.git
cd fastapi-ai-api-assignment
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Run Application

```bash
uvicorn app.main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### POST /summarize

Summarizes long text into a concise summary.

Request:

```json
{
  "text": "Artificial Intelligence is transforming industries..."
}
```

Response:

```json
{
  "summary": "Artificial Intelligence is transforming industries..."
}
```

---

### POST /translate

Translates text into a target language.

Request:

```json
{
  "text": "Hello",
  "target_language": "german"
}
```

Response:

```json
{
  "translated_text": "Hallo"
}
```

---

### POST /generate-email

Generates professional emails using AI.

Request:

```json
{
  "purpose": "Job Application for AI Intern",
  "recipient": "HR",
  "tone": "professional"
}
```

Response:

```json
{
  "generated_email": "Dear HR Team..."
}
```

---

## Logging

Application logs are stored in:

```text
logs/app.log
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Author

Smit Mukund Pandit
