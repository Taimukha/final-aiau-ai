import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Load API key from the project root .env file
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)


def ask_ai(prompt):
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in .env file")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "system",
                "content": "You are BookMatch AI, a friendly book recommendation assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content