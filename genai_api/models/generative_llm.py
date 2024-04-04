import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()


def llm(input_prompt):
    url = "https://api.openai.com/v1/chat/completions"
    api_key = os.getenv("OPENAI_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": input_prompt}],
        "temperature": 0,
        "max_tokens": 3000,
        "stream": False,
        "top_p": None,
    }

    response = requests.post(url, headers=headers, json=payload)
    print(response.status_code)

    data = response.json()
    text_output = data["choices"][0]["message"]["content"]
    return text_output
