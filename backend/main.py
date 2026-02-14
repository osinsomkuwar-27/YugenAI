from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from persona_extractor import extract_persona
from message_generator import generate_messages

app = FastAPI()

# --- CORS (IMPORTANT FOR REACT) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- REQUEST MODEL ---
class InputData(BaseModel):
    profile: str


@app.get("/")
def root():
    return {"status": "YugenAI Backend Running"}


# --- MAIN GENERATION ROUTE ---
@app.post("/generate")
def generate(data: InputData):

    profile_text = data.profile

    # Step 1: Persona Extraction
    persona = extract_persona(profile_text)

    # Step 2: Message Generation
    outputs = generate_messages(persona, profile_text)

    return {
        "persona": persona,
        "outputs": outputs
    }
