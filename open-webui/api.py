import requests

API_BASE_URL = "https://example.com/" # Replace with your actual API base URL
API_TOKEN = "xxxxxxxxx"  # Replace with your actual token


def chat_with_model(message):
    url = f"{API_BASE_URL}/api/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
      "model": "gemma3:4b",
      "messages": [
        {
          "role": "user",
          "content": f"{message}"
        }
      ]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

response_message = chat_with_model("Why is the sky blue?, answer in 1 sentence")["choices"][0]["message"]["content"]

print(response_message)