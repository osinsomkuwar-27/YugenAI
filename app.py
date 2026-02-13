import streamlit as st
import base64

# ⭐ BACKEND IMPORTS (MATCHES YOUR PROJECT)
from message_generator import generate_messages
from knowledge_base import save_record

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Shinobi Engine | Local LLM",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# LOAD LOCAL BACKGROUND IMAGE
# =========================================================
def load_bg(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

bg_img = load_bg("assets/naruto.png")

# =========================================================
# ENHANCED CSS (GLASSMORPHISM & MODERN UI)
# =========================================================
st.markdown(f"""
<style>
/* Background & Overlay */
[data-testid="stAppViewContainer"] {{
    background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url("data:image/png;base64,{bg_img}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* Hidden Header/Footer */
header {{visibility:hidden;}}
footer {{visibility:hidden;}}

/* Main Layout Padding */
.block-container {{
    padding-top: 2rem;
    padding-bottom: 2rem;
}}

/* Glass Cards */
.glass-card {{
    background: rgba(255, 255, 255, 0.07);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 20px;
}}

/* Custom Typography */
.main-title {{
    font-size: 42px;
    font-weight: 800;
    color: #FF9D00;
    margin-bottom: 5px;
    letter-spacing: -1px;
}}

.sub-title {{
    font-size: 16px;
    color: rgba(255,255,255,0.7);
    margin-bottom: 30px;
}}

/* Labels & Inputs */
label {{
    color: #FF9D00 !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}}

.stTextArea textarea, .stTextInput input {{
    background: rgba(0, 0, 0, 0.4) !important;
    color: #e0e0e0 !important;
    border: 1px solid rgba(255, 157, 0, 0.2) !important;
    border-radius: 12px !important;
}}

.stTextArea textarea:focus {{
    border-color: #FF9D00 !important;
}}

/* Tab Styling */
.stTabs [data-baseweb="tab-list"] {{
    gap: 10px;
    background-color: transparent;
}}

.stTabs [data-baseweb="tab"] {{
    height: 45px;
    white-space: pre-wrap;
    background-color: rgba(255,255,255,0.05);
    border-radius: 10px 10px 0px 0px;
    color: white;
    border: none;
    padding: 0px 20px;
}}

.stTabs [aria-selected="true"] {{
    background-color: rgba(255, 157, 0, 0.2) !important;
    border-bottom: 2px solid #FF9D00 !important;
}}

/* Custom Button */
.stButton>button {{
    width: 100%;
    background: linear-gradient(135deg, #FF9D00 0%, #FF4B2B 100%);
    color: white;
    border-radius: 12px;
    padding: 12px;
    font-weight: 700;
    border: none;
    transition: 0.3s;
    text-transform: uppercase;
}}

.stButton>button:hover {{
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(255, 157, 0, 0.4);
}}
</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================
if "generated" not in st.session_state:
    st.session_state.generated = False
if "results" not in st.session_state:
    st.session_state.results = None

# =========================================================
# SIDEBAR (CLEAN CONFIG)
# =========================================================
with st.sidebar:
    st.markdown("### 🛠️ Configuration")
    linkedin_url = st.text_input("Target URL", placeholder="https://linkedin.com/in/...")
    
    st.markdown("---")
    st.markdown("### 🏮 System Status")
    st.success("Local LLM: Online")
    st.info("Model: Shinobi-8B-v1")
    
    if st.button("Clear Cache"):
        st.session_state.results = None
        st.session_state.generated = False
        st.rerun()

# =========================================================
# MAIN CONTENT
# =========================================================
st.markdown('<div class="main-title">YugenAI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Local LLM Intelligence • Hyper-Personalized Sequences</div>', unsafe_allow_html=True)

left, right = st.columns([1, 1.2], gap="large")

# --- INPUT SECTION ---
with left:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 📥 Profile Analysis")
    
    profile_data = st.text_area(
        "Paste Profile Content", 
        height=350, 
        placeholder="Copy and paste the LinkedIn profile text here for the AI to analyze..."
    )

    st.write("")
    generate = st.button("Generate Outreach Sequence")
    st.markdown('</div>', unsafe_allow_html=True)

# --- BACKEND TRIGGER (UNTOUCHED LOGIC) ---
if generate and profile_data:
    with st.spinner("🍥 Gathering Chakra... (Generating via Local LLM)"):
        results = generate_messages(profile_data)
        
        # ⭐ SAVE TO KNOWLEDGE BASE (Exactly as per your request)
        save_record(
            results["persona"],
            {"combined_output": results["full_output"]}
        )

        st.session_state.results = results
        st.session_state.generated = True

# --- OUTPUT SECTION ---
with right:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### ✉️ Generated Assets")

    def extract_block(text, title):
        try:
            return text.split(f"=== {title} ===")[1].split("===")[0].strip()
        except:
            return "No output generated for this channel."

    if st.session_state.results:
        full_text = st.session_state.results["full_output"]
        
        # Tabbed interface for better UX
        tab1, tab2, tab3, tab4 = st.tabs(["📧 Email", "💼 LinkedIn", "💬 WhatsApp", "📸 Instagram"])
        
        with tab1:
            st.text_area("Subject & Body", extract_block(full_text, "EMAIL"), height=300, key="out_email")
        with tab2:
            st.text_area("Connection Request/DM", extract_block(full_text, "LINKEDIN"), height=300, key="out_li")
        with tab3:
            st.text_area("Direct Message", extract_block(full_text, "WHATSAPP"), height=300, key="out_wa")
        with tab4:
            st.text_area("DM Script", extract_block(full_text, "INSTAGRAM"), height=300, key="out_ig")
            
        st.success("Analysis Complete & Saved to Database")
    else:
        st.info("Awaiting input. Paste profile data and click generate to begin.")
        # Placeholder tabs for layout consistency
        st.tabs(["📧 Email", "💼 LinkedIn", "💬 WhatsApp", "📸 Instagram"])

    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER SUCCESS ---
if st.session_state.generated:
    st.toast("Messages generated and stored locally!", icon="✅")