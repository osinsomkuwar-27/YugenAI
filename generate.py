import requests

def generate_text(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)
    return response.json()["response"]

if __name__ == "__main__":
    prompt = "Write a short professional outreach email."
    output = generate_text(prompt)
    print(output)
