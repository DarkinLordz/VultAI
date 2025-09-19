from path import CONFIG_FILE, HISTORY_FILE, PERSONALITY_FILE
import requests
import json

def send_request(prompt):
    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        history = json.load(file)

    with open(PERSONALITY_FILE, "r", encoding="utf-8") as file:
        personality = file.read()

    url = data["url"]
    api = data["api"]
    model = data["model"]

    if url == "https://openrouter.ai/api/v1/chat/completions" or url == "https://api.groq.com/openai/v1/chat/completions":
        messages = [{"role": "system", "content": personality}] + history + [{"role": "user", "content": prompt}]

        headers = {"Authorization": f"Bearer {api}", "Content-Type": "application/json"}

        payload = {"model": model, "messages": messages}
        
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]