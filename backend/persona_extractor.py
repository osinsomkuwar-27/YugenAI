from llm_handler import ask_llm

def extract_persona(profile_text: str):

    prompt = f"""
    Extract structured persona from this profile:

    {profile_text}

    Return JSON:
    {{
        "name": "",
        "role": "",
        "seniority": "",
        "industry": "",
        "tone": "",
        "style_hint": "",
        "interests": []
    }}
    """

    result = ask_llm(prompt)

    try:
        import json
        return json.loads(result)
    except:
        return {
            "name": "Unknown",
            "role": "Professional",
            "seniority": "Mid",
            "industry": "General",
            "tone": "Neutral",
            "style_hint": "Direct",
            "interests": []
        }
