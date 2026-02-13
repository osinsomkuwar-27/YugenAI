import requests
from persona_extractor import extract_persona


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"


def generate_text(prompt):
    data = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.6,
            "num_predict": 250
        }
    }

    response = requests.post(OLLAMA_URL, json=data)
    return response.json()["response"]


def generate_messages(profile_text):

    persona = extract_persona(profile_text)

    base_prompt = f"""
You are an expert outreach copywriter.

STRICTLY use these details:
Name: {persona['name']}
Role: {persona['role']}
Industry: {persona['industry']}
Tone: {persona['tone']}
Style: {persona['style_hint']}
Interests: {", ".join(persona['interests'])}

Rules:
- Do NOT invent company names.
- Do NOT repeat sentences.
- Keep responses concise.
- Match the tone: {persona['tone']}.
- Include one clear CTA.
"""

    # Email
    email_prompt = base_prompt + """
Generate a personalized Cold Email.
Keep it under 120 words.
Include subject line.
"""

    # WhatsApp
    whatsapp_prompt = base_prompt + """
Generate a short WhatsApp message.
Keep it under 60 words.
Make it conversational.
"""

    # LinkedIn
    linkedin_prompt = base_prompt + """
Generate a LinkedIn DM.
Professional but friendly.
Keep it under 80 words.
"""

    # Instagram DM (NEW)
    instagram_prompt = base_prompt + """
Generate an Instagram DM.
Make it short, engaging, and slightly more casual than LinkedIn.
Keep it under 50 words.
Natural tone, not corporate.
"""

    return {
        "persona": persona,
        "email": generate_text(email_prompt),
        "whatsapp": generate_text(whatsapp_prompt),
        "linkedin": generate_text(linkedin_prompt),
        "instagram": generate_text(instagram_prompt)
    }


if __name__ == "__main__":

    sample_profile = """
    Rahul Sharma
    Founder at AI Labs
    Building AI automation tools for startups 🚀
    Passionate about AI, SaaS, and scaling fast.
    """

    results = generate_messages(sample_profile)

    print("\n===== Extracted Persona =====")
    print(results["persona"])

    print("\n===== Cold Email =====")
    print(results["email"])

    print("\n===== WhatsApp =====")
    print(results["whatsapp"])

    print("\n===== LinkedIn DM =====")
    print(results["linkedin"])

    print("\n===== Instagram DM =====")
    print(results["instagram"])
