from persona_extractor import extract_persona
from llm_handler import generate_with_llm
import random


def generate_messages(profile_text):

    persona = extract_persona(profile_text)

    # 🔥 Dynamic variation (prevents repetition)
    opening_styles = [
        "Start with curiosity.",
        "Start with appreciation.",
        "Start with a bold insight.",
        "Start with a friendly observation.",
        "Start with a short question."
    ]

    structure_styles = [
        "Use short punchy sentences.",
        "Use a storytelling tone.",
        "Use slightly persuasive structure.",
        "Keep it minimal and direct.",
        "Write like a natural human message."
    ]

    style_instruction = random.choice(opening_styles)
    structure_instruction = random.choice(structure_styles)

    # 🧠 BASE CONTEXT (UPGRADED)
    base_context = f"""
You are an expert outreach copywriter.

VERY IMPORTANT:
- Every output MUST feel NEW and ORIGINAL.
- Avoid template-style openings.
- Use different phrasing each time.
- Vary sentence structure.
- Do not reuse common cold outreach lines.

Person Details:
Name: {persona.get('name', '')}
Role: {persona.get('role', '')}
Industry: {persona.get('industry', '')}
Tone: {persona.get('tone', '')}
Interests: {", ".join(persona.get('interests', []))}

Writing Style Instructions:
{style_instruction}
{structure_instruction}

Rules:
- Do NOT invent company names.
- Match the tone exactly.
- Include exactly ONE clear CTA.
"""

    email_prompt = base_context + """
Write a UNIQUE Cold Email (under 120 words).
Include subject line.
Avoid generic openings like "I saw your profile".
"""

    whatsapp_prompt = base_context + """
Write a UNIQUE WhatsApp message (under 60 words).
Casual and conversational.
"""

    linkedin_prompt = base_context + """
Write a UNIQUE LinkedIn DM (under 80 words).
Professional but friendly.
"""

    instagram_prompt = base_context + """
Write a UNIQUE Instagram DM (under 60 words).
Short, engaging, slightly more casual.
"""

    # 🔥 Generate messages
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
