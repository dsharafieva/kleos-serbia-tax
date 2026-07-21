import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Kleos — Hiring a contractor in Serbia",
    page_icon="🇷🇸",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide default Streamlit chrome so the page renders full-bleed
st.markdown("""
<style>
  #MainMenu, header, footer {visibility: hidden;}
  .block-container {padding: 0 !important; max-width: 100% !important;}
  [data-testid="stAppViewContainer"] > .main {padding: 0 !important;}
  [data-testid="stHeader"] {display: none;}
</style>
""", unsafe_allow_html=True)

html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")

# Height must comfortably exceed the tallest rendered state (all sections
# expanded, SR strings, checklist ticked). Serbia runs a touch taller than
# Spain because of the nine-criterion checklist and longer independence-test copy.
components.html(html, height=6400, scrolling=True)
