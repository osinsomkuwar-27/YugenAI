import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"

def generate_with_llm(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.5,
                    "num_predict": 400   # Increased for full multi-message generation
                }
            },
            timeout=180  # Extra buffer for local model
        )

        response.raise_for_status()
        return response.json().get("response", "").strip()

    except requests.exceptions.Timeout:
        return "[LLM ERROR] Request timed out. Model took too long."

    except requests.exceptions.ConnectionError:
        return "[LLM ERROR] Could not connect to Ollama. Is it running?"

    except Exception as e:
        return f"[LLM ERROR] {str(e)}"
