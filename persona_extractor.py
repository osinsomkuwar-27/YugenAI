import re

def extract_persona(profile_text):
    persona = {}

    profile_text = profile_text.strip()
    lines = profile_text.split("\n")

    # Name
    persona["name"] = lines[0].strip() if len(lines) > 0 else "Unknown"

    # Role Detection
    if re.search(r"\bFounder\b", profile_text, re.IGNORECASE):
        persona["role"] = "Founder"
        persona["seniority"] = "Founder"
    elif re.search(r"\bSenior\b", profile_text, re.IGNORECASE):
        persona["role"] = "Senior Professional"
        persona["seniority"] = "Senior"
    elif re.search(r"\bManager\b", profile_text, re.IGNORECASE):
        persona["role"] = "Manager"
        persona["seniority"] = "Mid-level"
    else:
        persona["role"] = "Professional"
        persona["seniority"] = "Mid-level"

    # Industry Detection
    if re.search(r"\bAI\b|Artificial Intelligence", profile_text, re.IGNORECASE):
        persona["industry"] = "Artificial Intelligence"
    elif re.search(r"Fintech", profile_text, re.IGNORECASE):
        persona["industry"] = "Fintech"
    elif re.search(r"Marketing", profile_text, re.IGNORECASE):
        persona["industry"] = "Marketing"
    else:
        persona["industry"] = "General"

    # Tone Detection
    if any(emoji in profile_text for emoji in ["🚀", "🔥", "✨", "💡"]):
        persona["tone"] = "Casual"
        persona["emoji_usage"] = "High"
        persona["style_hint"] = "friendly and energetic"
    elif re.search(r"\bpassionate\b|\bbuilding\b", profile_text, re.IGNORECASE):
        persona["tone"] = "Semi-Casual"
        persona["emoji_usage"] = "Medium"
        persona["style_hint"] = "modern and conversational"
    else:
        persona["tone"] = "Professional"
        persona["emoji_usage"] = "Low"
        persona["style_hint"] = "formal and structured"

    # Interest Extraction
    keywords = ["AI", "Startups", "Automation", "Fintech", "SaaS", "Marketing"]
    interests = []
    for word in keywords:
        if re.search(word, profile_text, re.IGNORECASE):
            interests.append(word)

    persona["interests"] = interests if interests else ["Innovation"]

    return persona
