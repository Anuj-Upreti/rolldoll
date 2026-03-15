import streamlit as st

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="Roll Doll", layout="centered")

# ── Options data (edit here to change what appears) ───────────────────────────
OPTIONS = [
    {"number": "01", "title": "Roll", "desc": "Addition Practice."},
    {"number": "02", "title": "Doll", "desc": "Table Practice."},
]

# ── Minimal custom styling (limited in Streamlit) ─────────────────────────────
st.markdown("""
    <style>
        .block-container { max-width: 800px; padding-top: 4rem; }
        .title-label { font-size: 0.7rem; letter-spacing: 0.3em; color: #666; text-transform: uppercase; text-align: center; margin-bottom: 0.2rem; }
        .main-title  { font-size: 5rem; font-weight: 900; text-align: center; line-height: 1; margin-bottom: 0.5rem; }
        .subtitle    { font-size: 0.75rem; letter-spacing: 0.15em; color: #888; text-transform: uppercase; text-align: center; margin-bottom: 2.5rem; }
        .divider     { border: none; border-top: 1px solid #333; width: 3rem; margin: 0.8rem auto 1rem; }
    </style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<p class="title-label">Make a choice</p>', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">Title</h1>', unsafe_allow_html=True)
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Select one of the options below to continue</p>', unsafe_allow_html=True)

# ── Option buttons ────────────────────────────────────────────────────────────
col1, col2 = st.columns(2, gap="medium")

for col, option in zip([col1, col2], OPTIONS):
    with col:
        st.markdown(f"#### {option['number']} — {option['title']}")
        st.caption(option["desc"])
        if st.button(f"Select {option['title']}", key=option["number"], use_container_width=True):
            st.session_state["selected"] = option["title"]

# ── Show selection ────────────────────────────────────────────────────────────
if "selected" in st.session_state:
    st.divider()
    st.success(f"✅ You selected: **{st.session_state['selected']}**")