import streamlit as st
import base64

# ⭐ BACKEND IMPORTS (STAYING UNTOUCHED)
from message_generator import generate_messages
from knowledge_base import save_record

# =========================================================
# 01. PAGE CONFIG & SESSION INITIALIZATION
# =========================================================
st.set_page_config(
    page_title="Shinobi Engine v3 | Local LLM",
    page_icon="🏮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Crucial Fix: Initialize session state before any logic runs
if "results" not in st.session_state:
    st.session_state.results = None
if "generated" not in st.session_state:
    st.session_state.generated = False

# =========================================================
# 02. ASSETS & STYLING (THE SHINOBI UI)
# =========================================================
def load_bg(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except: return ""

bg_img = load_bg("assets/naruto.png")

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Orbitron:wght@400;900&display=swap');

    /* Background Setup with Dark Overlay */
    [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(180deg, rgba(10, 10, 15, 0.85) 0%, rgba(20, 10, 5, 0.95) 100%), url("data:image/png;base64,{bg_img}");
        background-size: cover;
        background-attachment: fixed;
    }}
    
    header, footer {{visibility: hidden;}}

    /* Futuristic HUD Styling */
    .main-header {{
        font-family: 'Orbitron', sans-serif;
        color: #FF9D00;
        font-size: 2.8rem;
        font-weight: 900;
        text-shadow: 0 0 20px rgba(255, 157, 0, 0.4);
        margin-bottom: 0px;
    }}

    .neon-text {{
        color: #00FFC2;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }}

    /* Card Panels (Glassmorphism + Terminal) */
    .terminal-card {{
        background: rgba(15, 15, 20, 0.65);
        border: 1px solid rgba(255, 157, 0, 0.2);
        border-radius: 8px;
        padding: 24px;
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }}

    /* Pulse Status Animation */
    @keyframes pulse {{
        0% {{ opacity: 0.4; }}
        50% {{ opacity: 1; }}
        100% {{ opacity: 0.4; }}
    }}
    .status-dot {{
        height: 10px;
        width: 10px;
        background-color: #00FFC2;
        border-radius: 50%;
        display: inline-block;
        margin-right: 10px;
        box-shadow: 0 0 10px #00FFC2;
        animation: pulse 2s infinite;
    }}

    /* Buttons */
    .stButton>button {{
        width: 100%;
        border-radius: 4px;
        border: 1px solid #FF9D00;
        background: rgba(255, 157, 0, 0.05);
        color: #FF9D00;
        font-family: 'Orbitron', sans-serif;
        padding: 15px;
        transition: 0.4s;
        letter-spacing: 2px;
    }}
    .stButton>button:hover {{
        background: #FF9D00;
        color: black;
        box-shadow: 0 0 30px rgba(255, 157, 0, 0.4);
    }}

    /* Tabs Override */
    .stTabs [data-baseweb="tab-list"] {{ gap: 8px; }}
    .stTabs [data-baseweb="tab"] {{
        background-color: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        padding: 8px 16px;
        border-radius: 4px 4px 0 0;
        color: #999;
    }}
    .stTabs [aria-selected="true"] {{
        color: #FF9D00 !important;
        border-color: #FF9D00 !important;
        background-color: rgba(255, 157, 0, 0.1) !important;
    }}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 03. SIDEBAR HUD (CONTROL CENTER)
# =========================================================
with st.sidebar:
    st.markdown("<h2 style='font-family:Orbitron; color:#FF9D00;'>S-RANK INTEL</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("<div class='neon-text'><span class='status-dot'></span>LOCAL LLM: ACTIVE</div>", unsafe_allow_html=True)
    st.progress(0.85, text="VRAM Utilization")
    
    st.divider()
    linkedin_url = st.text_input("🎯 Target URL", placeholder="Paste LinkedIn link...")
    
    st.caption("Engine Version: v3.0.1-Stable")
    if st.button("RESET SESSION"):
        st.session_state.results = None
        st.session_state.generated = False
        st.rerun()

# =========================================================
# 04. MAIN INTERFACE
# =========================================================
st.markdown('<div class="main-header">YugenAI</div>', unsafe_allow_html=True)
st.markdown('<div class="neon-text">Hyper-Personalized Local Intelligence Outreach</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

left_col, right_col = st.columns([1, 1.3], gap="large")

# --- LEFT: INPUT PANEL ---
with left_col:
    st.markdown('<div class="terminal-card">', unsafe_allow_html=True)
    st.markdown("<p class='neon-text' style='color:#FF9D00'>[ 01 ] INPUT_SIGNATURE</p>", unsafe_allow_html=True)
    
    profile_raw = st.text_area(
        "Lead Profile Data", 
        height=400, 
        placeholder="Paste LinkedIn Profile text, Biography, or Resume details here...",
        label_visibility="collapsed"
    )
    
    st.write("")
    if st.button("⚡ EXECUTE GENERATION"):
        if profile_raw:
            with st.spinner("🌀 WEAVING CHAKRA (LLM INFERENCE IN PROGRESS)..."):
                # ⭐ BACKEND CALLS (Original Logic)
                results = generate_messages(profile_raw)
                
                # Save to knowledge base as per your requirements
                save_record(
                    results["persona"],
                    {"combined_output": results["full_output"]}
                )
                
                # Update Session State
                st.session_state.results = results
                st.session_state.generated = True
        else:
            st.error("Input Data Required for Analysis.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- RIGHT: OUTPUT PANEL ---
with right_col:
    current_results = st.session_state.get("results")

    if current_results:
        # 1. ENHANCED PERSONA DOSSIER
        st.markdown('<div class="terminal-card">', unsafe_allow_html=True)
        st.markdown("<p class='neon-text' style='color:#00FFC2'>[ 02 ] STRATEGIC_DOSSIER</p>", unsafe_allow_html=True)
        
        persona = current_results.get("persona")
        
        # Check if persona is the dictionary you provided
        if isinstance(persona, dict):
            # Header with Name & Role
            st.markdown(f"### 🥷 {persona.get('name', 'Unknown')} | {persona.get('role', 'Professional')}")
            
            # Create a clean grid for metadata
            p_col1, p_col2 = st.columns(2)
            with p_col1:
                st.markdown(f"**Seniority:** `{persona.get('seniority')}`")
                st.markdown(f"**Industry:** `{persona.get('industry')}`")
            with p_col2:
                st.markdown(f"**Tone:** `{persona.get('tone')}`")
                st.markdown(f"**Style:** `{persona.get('style_hint')}`")
            
            # Interests as Neon Badges
            st.write("")
            interests = persona.get('interests', [])
            interest_html = "".join([f"<span class='persona-tag'># {i}</span>" for i in interests])
            st.markdown(interest_html, unsafe_allow_html=True)
            
        else:
            st.subheader(f"Persona: {persona}")
            
        st.markdown('</div>', unsafe_allow_html=True)

        # 2. GENERATED OUTREACH BLOCKS
        st.markdown('<div class="terminal-card">', unsafe_allow_html=True)
        st.markdown("<p class='neon-text' style='color:#FF9D00'>[ 03 ] OUTREACH_SCROLLS</p>", unsafe_allow_html=True)
        
        full_text = current_results.get("full_output", "")
        
        def extract(title):
            try: return full_text.split(f"=== {title} ===")[1].split("===")[0].strip()
            except: return "Section not found."

        tab_mail, tab_li, tab_wa, tab_ig = st.tabs(["📧 EMAIL", "💼 LINKEDIN", "💬 WHATSAPP", "📸 INSTA"])
        
        with tab_mail:
            st.code(extract("EMAIL"), language="markdown")
        with tab_li:
            st.code(extract("LINKEDIN"), language="markdown")
        with tab_wa:
            st.code(extract("WHATSAPP"), language="markdown")
        with tab_ig:
            st.code(extract("INSTAGRAM"), language="markdown")
            
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# 05. NOTIFICATIONS
# =========================================================
if st.session_state.generated:
    st.toast("Intelligence saved to Knowledge Base", icon="🏮")