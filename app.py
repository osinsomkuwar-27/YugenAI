import streamlit as st
import base64
import json # Added for the export feature

# ⭐ BACKEND IMPORTS (STAYING UNTOUCHED)
from message_generator import generate_messages
from knowledge_base import save_record

# =========================================================
# 01. PAGE CONFIG & SESSION INITIALIZATION
# =========================================================
st.set_page_config(
    page_title="YugenAI | Intelligence Engine",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize session state 
if "results" not in st.session_state:
    st.session_state.results = None
if "generated" not in st.session_state:
    st.session_state.generated = False

# =========================================================
# 02. ASSETS & STYLING (YUGEN AI + SHINOBI BACKGROUND)
# =========================================================
def load_bg(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except: return ""

# Make sure this path points to your actual image!
bg_img = load_bg("assets/naruto.png")

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Orbitron:wght@500;900&display=swap');

    /* Restored Background with Dark Gradient Overlay */
    [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(180deg, rgba(8, 8, 10, 0.85) 0%, rgba(15, 10, 5, 0.95) 100%), url("data:image/png;base64,{bg_img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #e0e0e0;
    }}
    
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}

    /* YugenAI Logo Styling */
    .logo-container {{
        text-align: center;
        margin-top: 2rem;
        margin-bottom: 3rem;
        user-select: none;
    }}
    .yugen-logo {{
        font-family: 'Orbitron', sans-serif;
        font-size: 5rem;
        font-weight: 900;
        color: #FF9D00;
        letter-spacing: -2px;
        line-height: 1;
        margin: 0;
        text-shadow: 0 0 20px rgba(255, 157, 0, 0.4);
    }}
    .yugen-ai {{
        color: #ffffff;
    }}
    .subtitle {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        color: #00FFC2;
        letter-spacing: 5px;
        text-transform: uppercase;
        margin-top: 10px;
    }}

    /* Terminal Cards with Glassmorphism */
    .terminal-card {{
        background: rgba(17, 17, 20, 0.75);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 157, 0, 0.15);
        border-radius: 6px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.6);
    }}
    
    /* Input Area Styling */
    .stTextArea textarea {{
        background-color: rgba(12, 12, 14, 0.8) !important;
        color: #00FFC2 !important;
        border: 1px solid rgba(255, 157, 0, 0.3) !important;
        font-family: 'JetBrains Mono', monospace !important;
        border-radius: 4px;
    }}
    .stTextArea textarea:focus {{
        border-color: #FF9D00 !important;
        box-shadow: 0 0 15px rgba(255, 157, 0, 0.3) !important;
    }}

    /* Primary Generate Button */
    .stButton>button {{
        width: 100%;
        background-color: rgba(255, 157, 0, 0.1);
        color: #FF9D00;
        font-family: 'Orbitron', sans-serif;
        font-weight: 700;
        font-size: 1rem;
        letter-spacing: 2px;
        border: 1px solid #FF9D00;
        border-radius: 4px;
        padding: 1rem;
        transition: all 0.3s ease;
    }}
    .stButton>button:hover {{
        background-color: #FF9D00;
        color: #000;
        box-shadow: 0 0 20px rgba(255, 157, 0, 0.5);
        transform: translateY(-2px);
    }}
    
    /* Secondary Buttons (Terminate / Download) */
    .btn-secondary .stButton>button, .stDownloadButton>button {{
        background-color: transparent !important;
        color: #00FFC2 !important;
        border: 1px solid #00FFC2 !important;
        padding: 0.5rem !important;
        font-size: 0.8rem !important;
    }}
    .btn-secondary .stButton>button:hover, .stDownloadButton>button:hover {{
        background-color: rgba(0, 255, 194, 0.1) !important;
        box-shadow: 0 0 10px rgba(0, 255, 194, 0.3) !important;
    }}

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 2rem;
        background-color: transparent;
    }}
    .stTabs [data-baseweb="tab"] {{
        color: #888;
        font-family: 'Orbitron', sans-serif;
        font-weight: 500;
        font-size: 0.9rem;
        letter-spacing: 1px;
        border: none;
        background: transparent;
        padding-bottom: 10px;
    }}
    .stTabs [aria-selected="true"] {{
        color: #FF9D00 !important;
        border-bottom: 2px solid #FF9D00 !important;
        text-shadow: 0 0 10px rgba(255,157,0,0.3);
    }}

    /* Metrics Override */
    [data-testid="stMetricValue"] {{
        font-family: 'JetBrains Mono', monospace;
        color: #00FFC2;
        font-size: 1.5rem;
    }}
    [data-testid="stMetricLabel"] {{
        font-family: 'Orbitron', sans-serif;
        color: #FF9D00;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}

    /* Data Grid Styling */
    .grid-label {{
        color: #888;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        text-transform: uppercase;
        margin-bottom: 4px;
    }}
    .grid-value {{
        color: #fff;
        font-size: 0.9rem;
        margin-bottom: 16px;
    }}
    .persona-tag {{
        color: #aaa;
        background: rgba(255,255,255,0.05);
        padding: 4px 8px;
        border-radius: 4px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
        margin-right: 8px;
        border: 1px solid rgba(255,255,255,0.1);
    }}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 03. HEADER UI
# =========================================================
st.markdown("""
<div class='logo-container'>
    <div class='yugen-logo'>YUGEN<span class='yugen-ai'>AI</span></div>
    <div class='subtitle'>Strategic Local Intelligence Engine</div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 04. MAIN INTERFACE LOGIC
# =========================================================

if not st.session_state.generated:
    # --- VIEW 1: INPUT TERMINAL ---
    st.markdown("<div style='color:#FF9D00; font-family:JetBrains Mono; margin-bottom: 10px;'>&gt; _ INTEL_INPUT</div>", unsafe_allow_html=True)
    
    profile_raw = st.text_area(
        "Input Data", 
        height=250, 
        placeholder="Paste Lead Persona data, Biography, or LinkedIn details here...",
        label_visibility="collapsed"
    )
    
    st.write("")
    if st.button("⚡ SYNC CHAKRA & GENERATE"):
        if profile_raw:
            with st.spinner("WEAVING INTEL..."):
                # ⭐ BACKEND CALLS
                results = generate_messages(profile_raw)
                save_record(results["persona"], {"combined_output": results["full_output"]})
                
                st.session_state.results = results
                st.session_state.generated = True
                st.rerun()
        else:
            st.error("Input Data Required for Analysis.")
    st.markdown("</div>", unsafe_allow_html=True)

else:
    # --- VIEW 2: RESULTS DASHBOARD ---
    current_results = st.session_state.get("results", {})
    persona = current_results.get("persona", {})
    
    # Top Control Bar
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.markdown("<div style='color:#FF9D00; font-family:JetBrains Mono; font-size: 0.9rem;'>🔓 S-RANK ACCESS<br><span style='color:#888; font-size: 0.7rem;'>UID: uba15zMBw4Xe...</span></div>", unsafe_allow_html=True)
    with col2:
        # NEW FEATURE: Export Button
        export_data = f"TARGET: {persona.get('name', 'Unknown')}\n---\n{current_results.get('full_output', '')}"
        st.download_button(
            label="💾 EXPORT",
            data=export_data,
            file_name=f"{persona.get('name', 'intel').replace(' ', '_')}_dossier.txt",
            mime="text/plain"
        )
    with col3:
        st.markdown('<div class="btn-secondary">', unsafe_allow_html=True)
        if st.button("⎋ TERMINATE"):
            st.session_state.generated = False
            st.session_state.results = None
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")

    # NEW FEATURE: HUD Metrics
    st.markdown("<div class='terminal-card' style='padding: 15px;'>", unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    m1.metric("Sync Alignment", "98.4%", "Optimal")
    m2.metric("Tokens Woven", "1,024", "Local LLM")
    m3.metric("Network Status", "SECURE", "Encrypted")
    st.markdown("</div>", unsafe_allow_html=True)

    # 1. ENHANCED PERSONA DOSSIER
    st.markdown("<div class='terminal-card' style='border-top: 2px solid #00FFC2;'>", unsafe_allow_html=True)
    st.markdown("<div style='color:#00FFC2; font-family:JetBrains Mono; margin-bottom:20px; font-size: 0.8rem;'>👤 PERSONA_DOSSIER</div>", unsafe_allow_html=True)
    
    name = persona.get('name', 'Unknown Target')
    role = persona.get('role', 'Professional')
    seniority = persona.get('seniority', 'Unknown Level')
    
    st.markdown(f"""
        <div style='display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; padding-bottom: 15px; margin-bottom: 15px;'>
            <div>
                <h2 style='margin: 0; font-family: Orbitron; font-weight: 700; font-size: 1.8rem; color: #fff;'>{name}</h2>
                <div style='color: #aaa; font-family: JetBrains Mono; font-size: 0.8rem; text-transform: uppercase; margin-top: 5px;'>{role}</div>
            </div>
            <div style='background: rgba(0, 255, 194, 0.1); color: #00FFC2; padding: 5px 12px; border-radius: 4px; font-family: JetBrains Mono; font-size: 0.7rem; border: 1px solid rgba(0,255,194,0.3);'>
                {seniority}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    g_col1, g_col2, g_col3 = st.columns(3)
    with g_col1:
        st.markdown(f"<div class='grid-label'>INDUSTRY</div><div class='grid-value'>{persona.get('industry', 'N/A')}</div>", unsafe_allow_html=True)
    with g_col2:
        st.markdown(f"<div class='grid-label'>TONE</div><div class='grid-value'>{persona.get('tone', 'N/A')}</div>", unsafe_allow_html=True)
    with g_col3:
        st.markdown(f"<div class='grid-label'>STYLE HINT</div><div class='grid-value'>{persona.get('style_hint', 'N/A')}</div>", unsafe_allow_html=True)
    
    interests = persona.get('interests', [])
    if interests:
        tags_html = "".join([f"<span class='persona-tag'>#{i.replace(' ', '').lower()}</span>" for i in interests])
        st.markdown(f"<div style='margin-top: 10px;'>{tags_html}</div>", unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. GENERATED OUTREACH BLOCKS
    st.markdown("<div class='terminal-card' style='border-top: 2px solid #FF9D00;'>", unsafe_allow_html=True)
    st.markdown("<div style='color:#FF9D00; font-family:JetBrains Mono; margin-bottom:10px; font-size: 0.8rem;'>🚀 OUTREACH_STRATEGY</div>", unsafe_allow_html=True)
    
    full_text = current_results.get("full_output", "")
    
    def extract(title):
        try: return full_text.split(f"=== {title} ===")[1].split("===")[0].strip()
        except: return f"// System Note: {title} block missing or malformed."

    tab_mail, tab_li, tab_wa, tab_ig = st.tabs(["EMAIL", "LINKEDIN", "WHATSAPP", "INSTAGRAM"])
    
    with tab_mail:
        st.code(extract("EMAIL"), language="markdown")
    with tab_li:
        st.code(extract("LINKEDIN"), language="markdown")
    with tab_wa:
        st.code(extract("WHATSAPP"), language="markdown")
    with tab_ig:
        st.code(extract("INSTAGRAM"), language="markdown")
        
    st.markdown('</div>', unsafe_allow_html=True)