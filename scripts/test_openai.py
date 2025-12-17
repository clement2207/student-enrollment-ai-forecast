import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # charge .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-4.1-mini",
    input="En une phrase, explique la différence entre un modèle interprétable et un modèle black-box."
)

print("OPENAI RESPONSE:")
print(response.output_text)

