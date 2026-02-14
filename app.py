import streamlit as st
import base64
import time

# ⭐ BACKEND IMPORTS (UNCHANGED)
from message_generator import generate_messages
from knowledge_base import save_record

# =========================================================
# 01. PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="YugenAI | S-RANK TERMINAL",
    page_icon="🏮",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "results" not in st.session_state:
    st.session_state.results = None
if "generated" not in st.session_state:
    st.session_state.generated = False

# =========================================================
# 02. ASSET LOADING
# =========================================================
def load_bg(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

bg_img = load_bg("assets/naruto.png")

# =========================================================
# 03. ADVANCED FUI & CSS ENGINE
# =========================================================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;500;700&family=Orbitron:wght@400;700;900&display=swap');

/* --- ROOT VARIABLES (STRICT PALETTE) --- */
:root {{
    --void: #020202;
    --orange: #FF9D00;
    --teal: #00FFC2;
    --magenta: #FF00FF;
    --glass: rgba(5, 5, 5, 0.85);
}}

/* --- GLOBAL RESET & BACKGROUND --- */
[data-testid="stAppViewContainer"] {{
    background-color: var(--void);
    background-image: url("data:image/png;base64,{bg_img}");
    background-size: cover;
    background-attachment: fixed;
    background-blend-mode: overlay;
}}

[data-testid="stHeader"] {{
    background: transparent;
}}

/* --- 1. VISUAL ARCHITECTURE --- */

/* Scanline 2.0 */
[data-testid="stAppViewContainer"]::after {{
    content: " ";
    position: fixed;
    top: 0; left: 0; width: 100vw; height: 100vh;
    background: linear-gradient(to bottom, rgba(255,255,255,0), rgba(255,255,255,0) 50%, rgba(0,0,0,0.2) 50%, rgba(0,0,0,0.2));
    background-size: 100% 4px;
    mix-blend-mode: overlay;
    pointer-events: none;
    z-index: 999;
    opacity: 0.6;
}}

/* Kinetic Neural Grid */
.neural-grid {{
    position: fixed;
    top: -50%; left: -50%; width: 200%; height: 200%;
    background-image: 
        linear-gradient(rgba(0, 255, 194, 0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 255, 194, 0.05) 1px, transparent 1px);
    background-size: 60px 60px;
    transform: perspective(500px) rotateX(60deg);
    animation: grid-fly 20s linear infinite;
    pointer-events: none;
    z-index: 0;
}}

@keyframes grid-fly {{
    0% {{ transform: perspective(500px) rotateX(60deg) translateY(0); }}
    100% {{ transform: perspective(500px) rotateX(60deg) translateY(60px); }}
}}

/* Chakra Aura Lighting */
.chakra-bloom {{
    position: fixed;
    border-radius: 50%;
    filter: blur(80px);
    opacity: 0.05;
    animation: breathe 10s ease-in-out infinite alternate;
    z-index: 0;
}}

@keyframes breathe {{
    0% {{ opacity: 0.02; transform: scale(0.8); }}
    100% {{ opacity: 0.08; transform: scale(1.2); }}
}}

/* --- 2. S-RANK TYPOGRAPHY --- */

.glitch-wrapper {{
    position: relative;
    display: inline-block;
    color: white;
    font-family: 'Orbitron', sans-serif;
    font-weight: 900;
    font-size: 4rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    margin-bottom: 0.5rem;
}}

/* Tri-Layer Glitch */
.glitch-text {{
    position: relative;
    z-index: 2;
    animation: text-flicker 3s infinite;
}}

.glitch-text::before, .glitch-text::after {{
    content: attr(data-text);
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    opacity: 0.8;
}}

.glitch-text::before {{
    color: var(--teal);
    z-index: -1;
    transform: translate(-2px, 0);
    clip-path: polygon(0 0, 100% 0, 100% 45%, 0 45%);
    animation: glitch-anim-1 2s infinite linear alternate-reverse;
}}

.glitch-text::after {{
    color: var(--orange);
    z-index: -2;
    transform: translate(2px, 0);
    clip-path: polygon(0 60%, 100% 60%, 100% 100%, 0 100%);
    animation: glitch-anim-2 2s infinite linear alternate-reverse;
}}

/* HUD Brackets */
.hud-bracket {{
    font-family: 'JetBrains Mono';
    color: var(--teal);
    font-size: 1rem;
    vertical-align: middle;
    margin: 0 15px;
    opacity: 0.8;
}}

.status-dot {{
    display: inline-block;
    width: 8px; height: 8px;
    background-color: var(--orange);
    border-radius: 50%;
    box-shadow: 0 0 10px var(--orange);
    animation: blink 1s infinite;
    margin-right: 10px;
}}

@keyframes text-flicker {{
    0% {{ opacity: 0.1; }}
    2% {{ opacity: 1; }}
    4% {{ opacity: 0.1; }}
    6% {{ opacity: 1; }}
    100% {{ opacity: 1; }}
}}

@keyframes blink {{ 50% {{ opacity: 0; }} }}

/* --- 3. GLASS-HUD CARDS & COMPONENTS --- */

/* Container Override */
.element-container {{
    z-index: 10;
}}

/* Custom Card Class for HTML injection */
.tactical-card {{
    background: var(--glass);
    backdrop-filter: blur(25px);
    border: 1px solid rgba(255, 157, 0, 0.1);
    position: relative;
    padding: 2rem;
    margin-bottom: 20px;
    /* Angled Geometry */
    clip-path: polygon(
        20px 0, 100% 0, 
        100% calc(100% - 20px), calc(100% - 20px) 100%, 
        0 100%, 0 20px
    );
    overflow: hidden;
}}

/* Tracing Border Animation */
.tactical-card::before {{
    content: '';
    position: absolute;
    top: -50%; left: -50%; width: 200%; height: 200%;
    background: conic-gradient(transparent, transparent, transparent, var(--teal));
    animation: radar-sweep 4s linear infinite;
    z-index: -1;
}}

.tactical-card::after {{
    content: '';
    position: absolute;
    inset: 1px; /* 1px border width */
    background: var(--glass);
    z-index: -1;
    clip-path: polygon(
        20px 0, 100% 0, 
        100% calc(100% - 20px), calc(100% - 20px) 100%, 
        0 100%, 0 20px
    );
}}

@keyframes radar-sweep {{
    0% {{ transform: rotate(0deg); }}
    100% {{ transform: rotate(360deg); }}
}}

/* --- 4. INTERACTIVE ELEMENTS (MICRO-UI) --- */

/* Tactical Text Area */
.stTextArea textarea {{
    background-color: rgba(0, 0, 0, 0.6) !important;
    color: var(--teal) !important;
    border: 1px solid rgba(0, 255, 194, 0.3) !important;
    font-family: 'JetBrains Mono' !important;
    border-radius: 0 !important;
    transition: all 0.3s ease;
    clip-path: polygon(0 0, 100% 0, 100% 90%, 95% 100%, 0 100%);
}}

.stTextArea textarea:focus {{
    border-color: var(--orange) !important;
    box-shadow: 0 0 25px rgba(255, 157, 0, 0.2), inset 0 0 10px rgba(255, 157, 0, 0.1) !important;
    transform: scale(1.005);
}}

/* Tactical Buttons */
.stButton > button {{
    background: linear-gradient(90deg, transparent 0%, rgba(255, 157, 0, 0.1) 50%, transparent 100%);
    border: 1px solid var(--orange) !important;
    color: var(--orange) !important;
    font-family: 'Orbitron' !important;
    font-weight: 700 !important;
    text-transform: uppercase;
    letter-spacing: 2px;
    padding: 1.5rem 0 !important;
    transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    position: relative;
    overflow: hidden;
}}

.stButton > button:hover {{
    background: var(--orange) !important;
    color: var(--void) !important;
    box-shadow: 0 0 30px var(--orange);
    animation: shake 0.3s cubic-bezier(.36,.07,.19,.97) both;
}}

@keyframes shake {{
    10%, 90% {{ transform: translate3d(-1px, 0, 0); }}
    20%, 80% {{ transform: translate3d(2px, 0, 0); }}
    30%, 50%, 70% {{ transform: translate3d(-4px, 0, 0); }}
    40%, 60% {{ transform: translate3d(4px, 0, 0); }}
}}

/* Tab Switches */
.stTabs [data-baseweb="tab-list"] {{
    gap: 10px;
    background: transparent;
}}

.stTabs [data-baseweb="tab"] {{
    background-color: rgba(255, 255, 255, 0.05);
    border: 1px solid #333;
    color: #666;
    font-family: 'JetBrains Mono';
    padding: 8px 20px;
    border-radius: 2px;
    transition: all 0.3s;
    clip-path: polygon(10px 0, 100% 0, 100% 100%, 0 100%, 0 10px);
}}

.stTabs [aria-selected="true"] {{
    background-color: rgba(0, 255, 194, 0.1) !important;
    border: 1px solid var(--teal) !important;
    color: var(--teal) !important;
    text-shadow: 0 0 10px var(--teal);
    box-shadow: inset 0 0 15px rgba(0, 255, 194, 0.1);
}}

/* Sidebar Styling */
[data-testid="stSidebar"] {{
    background-color: var(--void);
    border-right: 1px solid rgba(255, 157, 0, 0.2);
}}

.sidebar-stat {{
    font-family: 'JetBrains Mono';
    font-size: 0.8rem;
    color: #666;
    margin-bottom: 5px;
    display: flex;
    justify-content: space-between;
}}

.sidebar-val {{
    color: var(--teal);
}}

hr {{
    border-color: rgba(255, 157, 0, 0.2);
}}

/* Scrollbar */
::-webkit-scrollbar {{ width: 6px; }}
::-webkit-scrollbar-track {{ background: var(--void); }}
::-webkit-scrollbar-thumb {{ background: var(--orange); border-radius: 2px; }}

</style>

<!-- BACKGROUND LAYERS -->
<div class="neural-grid"></div>
<div class="chakra-bloom" style="top: -10%; left: -10%; width: 50vw; height: 50vw; background: radial-gradient(circle, var(--orange), transparent 70%);"></div>
<div class="chakra-bloom" style="bottom: -10%; right: -10%; width: 60vw; height: 60vw; background: radial-gradient(circle, var(--teal), transparent 70%);"></div>
""", unsafe_allow_html=True)

# =========================================================
# 04. SIDEBAR HUD
# =========================================================
with st.sidebar:
    st.markdown("""
        <div style="font-family:'Orbitron'; color:#FF9D00; font-size:1.4rem; border-bottom:1px solid #FF9D00; padding-bottom:10px; margin-bottom:20px;">
        ⚡ YUGEN_CORE
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-stat"><span>CPU_THREAD_01</span><span class="sidebar-val">ACTIVE</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-stat"><span>NEURAL_LINK</span><span class="sidebar-val">SECURE</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-stat"><span>CHAKRA_LEVEL</span><span class="sidebar-val">98.4%</span></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.progress(0.85)
    st.caption("SYSTEM INTEGRITY")
    
    st.markdown("---")
    st.markdown("<span style='color:var(--magenta); font-family:Orbitron; font-size:0.7rem;'>WARNING: S-RANK AUTHORIZATION REQUIRED FOR DEEP SCAN</span>", unsafe_allow_html=True)

# =========================================================
# 05. MAIN INTERFACE
# =========================================================

# --- HEADER SECTION ---
st.markdown("""
    <div style="text-align:center; padding-top: 2rem;">
        <div class="hud-bracket">[ <span class="status-dot"></span> SYSTEM_ONLINE ]</div>
        <div class="glitch-wrapper">
            <div class="glitch-text" data-text="YUGEN_AI">YUGEN_AI</div>
        </div>
        <div class="hud-bracket">[ TACTICAL INTELLIGENCE TERMINAL ]</div>
    </div>
""", unsafe_allow_html=True)

st.write("") # Spacer

left_col, right_col = st.columns([1, 1.4], gap="large")

# --- LEFT COLUMN: COMMAND CONSOLE ---
with left_col:
    st.markdown("""
    <div style="margin-bottom: 10px; font-family:'Orbitron'; color:var(--orange); letter-spacing:2px; font-size:0.8rem;">
        // INPUT_VECTOR: TARGET_DATA
    </div>
    """, unsafe_allow_html=True)
    
    # We rely on Streamlit's default widget styling via CSS injection for this part
    profile_raw = st.text_area(
        "label_hidden",
        height=450,
        placeholder="> PASTE TARGET DOSSIER HERE\n> AWAITING TEXT STREAM...",
        label_visibility="collapsed",
        key="tactical_input"
    )
    
    st.write("")
    
    if st.button("⚡ INITIATE_SHINOBI_PROTOCOL"):
        if profile_raw:
            with st.spinner("Decoding Chakra Signature..."):
                # Simulation
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.015)
                    progress_bar.progress(i + 1)
                
                results = generate_messages(profile_raw)
                save_record(results["persona"], {"combined_output": results["full_output"]})
                st.session_state.results = results
                st.session_state.generated = True
        else:
            st.error(">> CRITICAL ERROR: NO DATA VECTOR DETECTED")

# --- RIGHT COLUMN: INTELLIGENCE DOSSIER ---
with right_col:
    current_results = st.session_state.get("results")

    if current_results:
        persona = current_results.get("persona")
        
        # S-RANK HEADER CARD
        if isinstance(persona, dict):
            st.markdown(f"""
            <div class="tactical-card">
                <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                    <div>
                        <div style="font-family:'Orbitron'; color:var(--orange); font-size:2rem; line-height:1;">
                            {persona.get('name', 'UNKNOWN').upper()}
                        </div>
                        <div style="font-family:'JetBrains Mono'; color:var(--teal); font-size:0.9rem; margin-top:5px;">
                            CLASS: {persona.get('role', 'ROGUE').upper()}
                        </div>
                    </div>
                    <div style="border:1px solid var(--orange); padding:5px 10px; color:var(--orange); font-family:'Orbitron'; font-size:0.7rem;">
                        S-RANK
                    </div>
                </div>
                <div style="margin-top:15px; border-top:1px dashed rgba(255,255,255,0.2); padding-top:10px;">
                    {''.join([f'<span style="background:rgba(0,255,194,0.1); color:var(--teal); border:1px solid var(--teal); padding:2px 8px; font-size:0.7rem; font-family:JetBrains Mono; margin-right:5px; margin-bottom:5px; display:inline-block;">#{i}</span>' for i in persona.get('interests', [])])}
                </div>
            </div>
            """, unsafe_allow_html=True)

        # CONTENT EXTRACTION
        full_text = current_results.get("full_output", "")
        def extract(title):
            try:
                return full_text.split(f"=== {title} ===")[1].split("===")[0].strip()
            except:
                return "DATA_CORRUPTED_OR_MISSING"

        # TABS INTERFACE
        tab_mail, tab_li, tab_wa, tab_ig = st.tabs(["[ EMAIL ]", "[ LINKEDIN ]", "[ WHATSAPP ]", "[ INSTAGRAM ]"])

        def render_data_card(content, type_label):
            return f"""
            <div class="tactical-card" style="animation: fade-in 0.5s ease-out;">
                <div style="font-family:'JetBrains Mono'; color:#666; font-size:0.7rem; margin-bottom:10px;">
                    // DECRYPTED_{type_label}_PACKET
                </div>
                <div style="font-family:'JetBrains Mono'; color:var(--teal); font-size:0.9rem; white-space:pre-wrap; line-height:1.6;">{content}</div>
            </div>
            """

        with tab_mail:
            st.markdown(render_data_card(extract('EMAIL'), "SMTP"), unsafe_allow_html=True)
        
        with tab_li:
            st.markdown(render_data_card(extract('LINKEDIN'), "LI_NET"), unsafe_allow_html=True)

        with tab_wa:
            st.markdown(render_data_card(extract('WHATSAPP'), "VOIP"), unsafe_allow_html=True)

        with tab_ig:
            st.markdown(render_data_card(extract('INSTAGRAM'), "IMAGE"), unsafe_allow_html=True)

    else:
        # IDLE STATE
        st.markdown("""
        <div class="tactical-card" style="height: 500px; display:flex; align-items:center; justify-content:center; flex-direction:column; border:1px dashed rgba(255,157,0,0.3);">
            <div style="font-size:3rem; margin-bottom:20px; animation: breathe 3s infinite;">🏮</div>
            <div style="font-family:'Orbitron'; color:rgba(255,157,0,0.5); font-size:1.5rem;">AWAITING UPLINK</div>
            <div style="font-family:'JetBrains Mono'; color:rgba(0,255,194,0.3); font-size:0.8rem; margin-top:10px;">// SYSTEM IDLE</div>
        </div>
        """, unsafe_allow_html=True)

if st.session_state.generated:
    st.toast(">> MISSION ACCOMPLISHED: INTEL SECURED", icon="💾")