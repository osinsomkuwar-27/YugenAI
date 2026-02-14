from llm_handler import ask_llm

def generate_messages(persona, profile_text):

    prompt = f"""
    Create outreach messages based on persona:

    Persona:
    {persona}

    Profile:
    {profile_text}

    Return JSON:
    {{
        "EMAIL": "",
        "LINKEDIN": "",
        "WHATSAPP": "",
        "INSTAGRAM": ""
    }}
    """

    result = ask_llm(prompt)

    try:
        import json
        return json.loads(result)
    except:
        return {
            "EMAIL": "Failed to generate",
            "LINKEDIN": "",
            "WHATSAPP": "",
            "INSTAGRAM": ""
        }
