import os
from dataclasses import dataclass
from typing import Literal, Optional

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

Provider = Literal["mock", "openai"]

@dataclass
class AIConfig:
    provider: Provider = "mock"
    model: Optional[str] = "gpt-4.1-mini"

def explain_forecast(
    summary: str,
    config: AIConfig = AIConfig()
) -> str:

    if config.provider == "mock":
        return (
            "AI Summary (mock):\n"
            "- The forecast is driven by the growth coefficient r(t).\n"
            "- Small variations in r(t) significantly affect enrollment.\n"
            "- This illustrates the importance of demographic sensitivity.\n\n"
            f"Context received:\n{summary}"
        )

    if config.provider == "openai":
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        prompt = f"""
You are an AI assistant specialized in education analytics.

Given the following enrollment forecast data,
provide a concise and clear interpretation for decision-makers.

{summary}
"""

        response = client.chat.completions.create(
            model=config.model,
            messages=[
                {"role": "system", "content": "You are a data analyst AI."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4,
        )

        return response.choices[0].message.content

    raise ValueError("Unknown provider")
