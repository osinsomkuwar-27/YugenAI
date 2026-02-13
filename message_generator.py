from persona_extractor import extract_persona
from llm_handler import generate_with_llm


def generate_messages(profile_text):

    persona = extract_persona(profile_text)

    base_prompt = f"""
You are an expert outreach copywriter.

STRICTLY use these details:
Name: {persona.get('name', '')}
Role: {persona.get('role', '')}
Industry: {persona.get('industry', '')}
Tone: {persona.get('tone', '')}
Interests: {", ".join(persona.get('interests', []))}

Rules:
- Do NOT invent company names.
- Do NOT repeat sentences.
- Keep responses concise.
- Match the tone: {persona.get('tone', '')}.
- Each message must include one clear CTA.
"""

    # 📧 Cold Email
    email_prompt = base_prompt + """
Generate a personalized Cold Email.
Keep it under 120 words.
Include subject line.
"""

    # 💬 WhatsApp
    whatsapp_prompt = base_prompt + """
Generate a short WhatsApp message.
Keep it under 60 words.
Make it conversational.
"""

    # 🔗 LinkedIn DM
    linkedin_prompt = base_prompt + """
Generate a LinkedIn DM.
Professional but friendly.
Keep it under 80 words.
"""

    # 📸 Instagram DM
    instagram_prompt = base_prompt + """
Generate an Instagram DM.
Keep it short, engaging, slightly casual.
Under 70 words.
Sound natural and friendly.
"""

    return {
        "persona": persona,
        "email": generate_with_llm(email_prompt),
        "whatsapp": generate_with_llm(whatsapp_prompt),
        "linkedin": generate_with_llm(linkedin_prompt),
        "instagram": generate_with_llm(instagram_prompt)
    }
