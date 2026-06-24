from groq import Groq
from app.core.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def generate_email(
    purpose: str,
    recipient: str,
    tone: str,
):
    prompt = f"""
You are an expert corporate email writer.

Write a complete, professional, well-formatted email based on the details below.

Purpose:
{purpose}

Recipient:
{recipient}

Tone:
{tone}

Requirements:
1. Generate a relevant and professional Subject line.
2. Start with an appropriate greeting.
3. Write a clear introduction.
4. Write a detailed but concise body.
5. End with a professional closing.
6. Use proper business email etiquette.
7. Make the email natural and human-like.
8. Avoid placeholders such as [Your Name].
9. Return ONLY the email.

Output Format:

Subject: <subject>

Dear <recipient>,

<email body>

Best regards,
AI Assistant
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
You are a senior executive assistant with 15+ years of experience
writing professional business emails.

Your emails should be:
- Polite
- Professional
- Grammatically correct
- Well structured
- Human sounding
- Action oriented when necessary
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4,
        max_tokens=700,
    )

    return response.choices[0].message.content.strip()