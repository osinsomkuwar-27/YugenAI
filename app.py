import streamlit as st
import base64

# ⭐ BACKEND IMPORTS (MATCHES YOUR PROJECT)
from message_generator import generate_messages
from knowledge_base import save_record

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Offline LLM Outreach Engine",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# LOAD LOCAL BACKGROUND IMAGE
# =========================================================
def load_bg(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_img = load_bg("assets/naruto.png")

# =========================================================
# GLOBAL CSS
# =========================================================
st.markdown(f"""
<style>

[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/png;base64,{bg_img}");
    background-size: cover;
    background-position: center;
}}

header {{visibility:hidden;}}
footer {{visibility:hidden;}}

.block-container {{
    padding-top:30px;
    padding-left:70px;
    padding-right:70px;
}}

.main-header {{
    background: rgba(255,230,180,0.9);
    padding:18px 28px;
    border-radius:14px;
    font-size:30px;
    font-weight:800;
    color:black;
}}

.sub-header {{
    margin-top:14px;
    background: rgba(0,0,0,0.65);
    padding:14px 22px;
    border-radius:14px;
    font-size:20px;
    font-weight:600;
    color:white;
}}

.grey-strip {{
    height:46px;
    background: rgba(80,80,80,0.6);
    border-radius:24px;
    margin-top:22px;
    margin-bottom:28px;
}}

.section-title {{
    font-size:26px;
    font-weight:700;
    color:black !important;
    margin-bottom:10px;
}}

.card {{
    background: rgba(255,255,255,0.12);
    padding:24px;
    border-radius:18px;
    backdrop-filter: blur(10px);
}}

label {{
    color:black !important;
    font-weight:600 !important;
}}

input, textarea {{
    background:#32353d !important;
    color:white !important;
    border-radius:16px !important;
    border:none !important;
}}

.stButton>button {{
    background:#6a3d2c;
    color:white;
    border-radius:16px;
    padding:14px 26px;
    font-size:18px;
    border:none;
}}

.stButton>button:hover {{
    background:#7d4a36;
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
# HEADER
# =========================================================
st.markdown(
    '<div class="main-header">Offline LLM Outreach Engine</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-header">Generate hyper-personalized outreach using local AI</div>',
    unsafe_allow_html=True
)

c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="grey-strip"></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="grey-strip"></div>', unsafe_allow_html=True)

# =========================================================
# MAIN GRID
# =========================================================
left, right = st.columns(2, gap="large")

# =========================================================
# INPUT SECTION
# =========================================================
with left:
    st.markdown('<div class="section-title">Input Section</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)

    linkedin_url = st.text_input("Paste LinkedIn Profile URL")
    profile_data = st.text_area("Paste Profile Data", height=200)

    st.write("")
    generate = st.button("Generate Message")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# GENERATE ACTION (CONNECTED TO BACKEND)
# =========================================================
if generate and profile_data:

    with st.spinner("Generating outreach using Local LLM..."):

        results = generate_messages(profile_data)

        # ⭐ SAVE TO KNOWLEDGE BASE
        save_record(
            results["persona"],
            {"combined_output": results["full_output"]}
        )

        st.session_state.results = results
        st.session_state.generated = True

# =========================================================
# OUTPUT SECTION
# =========================================================
with right:
    st.markdown('<div class="section-title">Generated Outreach</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)

    def extract_block(text, title):
        try:
            return text.split(f"=== {title} ===")[1].split("===")[0].strip()
        except:
            return ""

    if st.session_state.results:

        full_text = st.session_state.results["full_output"]

        st.text_area("Email Output", extract_block(full_text, "EMAIL"), height=100)
        st.text_area("Linkedin DM", extract_block(full_text, "LINKEDIN"), height=100)
        st.text_area("WhatsApp Message", extract_block(full_text, "WHATSAPP"), height=100)
        st.text_area("Instagram DM", extract_block(full_text, "INSTAGRAM"), height=100)

    else:
        st.text_area("Email Output", "", height=100)
        st.text_area("Linkedin DM", "", height=100)
        st.text_area("WhatsApp Message", "", height=100)
        st.text_area("Instagram DM", "", height=100)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# SUCCESS MESSAGE
# =========================================================
if st.session_state.generated:
    st.success("Outreach Messages Generated Successfully")
