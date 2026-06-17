from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv(override=True)

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Generate IQ Question
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": "Ask one logical IQ question."
        }
    ]
)

question = response.choices[0].message.content

print("\nQuestion:")
print(question)

# Answer the Question
answer_response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": f"Answer this IQ question:\n\n{question}"
        }
    ]
)

print("\nAnswer:")
print(answer_response.choices[0].message.content)