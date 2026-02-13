🚀 PersonaForge
Offline LLM-Powered Hyper-Personalized Cold Outreach Engine

Problem Statement ID: SBM02 – Social Booster Media Domain
Xenia Hackathon 2026

📌 Overview

Cold outreach is widely used to connect with potential customers, partners, and talent. However, most outreach today is:

❌ Generic

❌ Poorly personalized

❌ Tone-mismatched

❌ Dependent on cloud AI APIs

❌ Not privacy-focused

PersonaForge is a fully offline, privacy-first LLM-powered outreach engine that generates hyper-personalized, tone-adaptive, multi-channel outreach messages using structured persona modeling.

🎯 Problem Statement

Design and build a cold outreach automation tool that:

Runs entirely on an offline LLM

Generates multi-channel personalized outreach

Adapts tone based on recipient communication style

Stores and reuses previous outreach knowledge

Does NOT rely on external AI APIs

💡 Our Solution

Our system:

Accepts LinkedIn profile text (or mock profile data)

Extracts structured persona information

Infers:

Seniority

Industry

Communication tone

Language style

Uses an offline LLM to generate:

📧 Cold Email

💬 WhatsApp Message

🔗 LinkedIn DM

Stores persona + generated messages locally for knowledge reuse

🏗 System Architecture
User Input (LinkedIn Profile Text)
        ↓
Persona Extraction Module
        ↓
Offline LLM (Mistral / LLaMA via Ollama)
        ↓
Multi-Channel Message Generator
        ↓
Local Knowledge Base (JSON)
        ↓
Streamlit UI

🛠 Tech Stack
🔹 Backend

Python 3.10+

Ollama (Offline LLM Runtime)

Mistral 7B / LLaMA 3

JSON-based Knowledge Base

🔹 Frontend

Streamlit

🔹 AI Engine

Open-source LLM running locally

Prompt-engineered persona extraction

Tone-adaptive message generation

🔹 Tools

GitHub

VS Code

📂 Project Structure
persona-forge/
│
├── app.py
├── persona_extractor.py
├── message_generator.py
├── knowledge_base.json
├── requirements.txt
└── README.md

🤖 AI & Personalization Logic
1️⃣ Persona Modeling

From LinkedIn profile text, the system extracts:

Name

Role

Company

Industry

Seniority

Communication tone (casual / formal / mixed)

Emoji usage

Language style

Interests

Example Persona JSON:

{
  "name": "Rahul Sharma",
  "role": "Founder",
  "company": "AI Startup",
  "industry": "Artificial Intelligence",
  "seniority": "Decision Maker",
  "tone": "Semi-casual",
  "emoji_usage": "Low",
  "language_style": "Professional English",
  "interests": ["AI", "Automation", "Startups"]
}

2️⃣ Multi-Channel Message Generation

For each persona, the system generates:

Personalized Cold Email

WhatsApp Message

LinkedIn DM

Each message is:

Highly personalized

Tone-matched

CTA-focused

Human-like and non-generic

3️⃣ Knowledge Base System

The system stores:

Previously targeted personas

Generated outreach messages

Industry metadata

This enables smarter outreach for similar prospects in the future.

🔐 Why Offline LLM?

Unlike cloud-based AI tools:

✅ No external API calls

✅ No data leaves the system

✅ Zero per-message cost

✅ Fully privacy-focused

✅ Compliant with hackathon constraints

🖥 Installation & Setup
1️⃣ Install Python Dependencies
pip install -r requirements.txt


If requirements.txt not created yet:

pip install streamlit ollama

2️⃣ Install Ollama

Download from:

👉 https://ollama.com/download

Verify installation:

ollama --version

3️⃣ Pull LLM Model
ollama run mistral


(The model downloads automatically on first run.)

4️⃣ Run the Application
streamlit run app.py

📸 Demo Flow

Paste LinkedIn profile text

Click Generate Outreach

View extracted persona

View:

Email

WhatsApp

LinkedIn DM

Data saved locally in knowledge_base.json

🚀 Key Highlights

🔥 Fully offline LLM deployment

🎯 Tone-adaptive personalization

🔐 Privacy-first architecture

📈 Multi-channel automation

🧠 Knowledge reuse capability

👥 Team Members

Rushikesh – Offline LLM Setup

Soham – Persona Extractor

Osin – Message Generator

Shreeja – UI Development

Kshitij – Knowledge Base & Integration

📄 License

This project is developed for Xenia Hackathon 2026 demonstration purposes only.
