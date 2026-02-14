from persona_extractor import extract_persona
from llm_handler import generate_with_llm
import random


def generate_messages(profile_text):

    persona = extract_persona(profile_text)

    # 🔥 Dynamic variation (prevents repetition)
    opening_styles = [
    "Start with gentle curiosity.",
    "Start with appreciation.",
    "Start with a calm observation.",
    "Start naturally, like a real person.",
    "Start with a simple question."
]

    structure_styles = [
    "Use short, relaxed sentences.",
    "Keep the tone calm and human.",
    "Avoid marketing language.",
    "Keep it minimal and gentle.",
    "Write like a real human, not a brand."
]

    style_instruction = random.choice(opening_styles)
    structure_instruction = random.choice(structure_styles)

    # 🧠 BASE CONTEXT (UPGRADED)
    base_context = f"""
You are a polite, thoughtful human reaching out for the first time.
You are not selling anything.
You are only starting a conversation.

VERY IMPORTANT:
- Every output MUST feel NEW and ORIGINAL.
- Avoid template-style openings.
- Use different phrasing each time.
- Vary sentence structure.
- Do not reuse common cold outreach lines.
- No selling language.
- No pitching.
- No urgency.
- No hype words.
- No business buzzwords.

Person Details:
Name: {persona.get('name', '')}
Role: {persona.get('role', '')}
Industry: {persona.get('industry', '')}
Tone: {persona.get('tone', '')}
Interests: {", ".join(persona.get('interests', []))}
Likely Context: Busy professional with limited time.

Tone Enforcement:
- If tone is "soft": be extra polite and gentle.
- If tone is "neutral": friendly and calm.
- If tone is "energetic": light enthusiasm only.

Writing Style Instructions:
{style_instruction}
{structure_instruction}

Rules:
- Do NOT invent company names.
- Match the tone exactly.
- End with a soft, optional question.
- The question must be easy to ignore without pressure.
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
