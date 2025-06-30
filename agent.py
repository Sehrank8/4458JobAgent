import httpx
import os
from dotenv import load_dotenv
import json

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
SEARCH_API_URL = os.getenv("SEARCH_API_URL")


def extract_query_from_llm(message: str) -> dict:
    prompt = f"""
    Extract the job search parameters from the user message below.
    Do NOT include any markdown code fences like ``` or ```json
    JUST GIVE A RAW JSON WITHOUT MARKDOWN CODE.
    User: {message}
    Your response MUST be ONLY valid JSON WITH NO MARKDOWN in this format:
    {{
      "city": "city name",
      "title": "job title"
    }}

    NO explanation. NO comments. NO code. NO extra text. DO NOT include JSON:.
    Return JUST ONE raw JSON and nothing else. DO NOT say Response: and DO NOT use ```
    Do NOT include any markdown code fences like ``` or ```json
    Your response MUST be ONLY valid JSON in this format:
    {{
      "city": "city name",
      "title": "job title"
    }}
    
    """

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "deepseek-ai/DeepSeek-V3",
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.4,
    }

    response = httpx.post("https://api.together.xyz/v1/completions", json=body, headers=headers)
    result_text = response.json()["choices"][0]["text"]

    try:
        print("       ", result_text)

        return json.loads(result_text.strip())
    except json.JSONDecodeError:
        print("JSON parse error:", result_text)
        return {}


def search_jobs(city, title):
    params = {
        "city": city,
        "title": title,
        "userId": "agent",  # fake user for logging
        "page": 0,
        "size": 3
    }

    response = httpx.get(SEARCH_API_URL, params=params)
    return response.json()
