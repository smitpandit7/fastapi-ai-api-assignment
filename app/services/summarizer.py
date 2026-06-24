from groq import Groq
from app.core.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def summarize_text(text: str):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Summarize the given text clearly in 3-4 lines."
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content