from persona_extractor import extract_persona
from llm_handler import generate_with_llm


def generate_messages(profile_text):

    persona = extract_persona(profile_text)

    base_context = f"""
You are an expert outreach copywriter.

Person Details:
Name: {persona.get('name', '')}
Role: {persona.get('role', '')}
Industry: {persona.get('industry', '')}
Tone: {persona.get('tone', '')}
Interests: {", ".join(persona.get('interests', []))}

Rules:
- Do NOT invent company names.
- Do NOT repeat sentences.
- Match the tone exactly.
- Include exactly ONE clear CTA.
"""

    email_prompt = base_context + """
Write a Cold Email (under 120 words).
Include subject line.
"""

    whatsapp_prompt = base_context + """
Write a WhatsApp message (under 60 words).
Casual and conversational.
"""

    linkedin_prompt = base_context + """
Write a LinkedIn DM (under 80 words).
Professional but friendly.
"""

    instagram_prompt = base_context + """
Write an Instagram DM (under 60 words).
Short, engaging, slightly more casual.
"""

    email = generate_with_llm(email_prompt)
    whatsapp = generate_with_llm(whatsapp_prompt)
    linkedin = generate_with_llm(linkedin_prompt)
    instagram = generate_with_llm(instagram_prompt)

    full_output = f"""
=== EMAIL ===
{email}

=== WHATSAPP ===
{whatsapp}

=== LINKEDIN ===
{linkedin}

=== INSTAGRAM ===
{instagram}
"""

    return {
        "persona": persona,
        "full_output": full_output
    }
