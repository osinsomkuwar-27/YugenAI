from persona_extractor import extract_persona
from llm_handler import generate_with_llm


def generate_messages(profile_text):

    persona = extract_persona(profile_text)

    combined_prompt = f"""
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

Now generate ALL of the following clearly separated with headings:

1. Cold Email (under 120 words, include subject line)
2. WhatsApp Message (under 60 words)
3. LinkedIn DM (under 80 words)
4. Instagram DM (under 70 words)

Format exactly like this:

=== EMAIL ===
<email here>

=== WHATSAPP ===
<whatsapp here>

=== LINKEDIN ===
<linkedin here>

=== INSTAGRAM ===
<instagram here>
"""

    full_output = generate_with_llm(combined_prompt)

    return {
        "persona": persona,
        "full_output": full_output
    }
