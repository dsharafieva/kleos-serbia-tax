"""
Kleos — Serbia contractor guide
Streamlit wrapper. Renders index.html so the calculator, the
nine-criterion checklist and the FAQ accordion are interactive.

The page is a fixed-width (1440px) Figma export, so it is served
as-is inside a component iframe rather than rebuilt with Streamlit
widgets. Editing app.py does not change the design; edit index.html.
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

PAGE_HEIGHT = 8300  # index.html is ~8113px; a little slack avoids clipping

st.set_page_config(
    page_title="Hire contractors in Serbia: tax and the independence test | Kleos",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Strip Streamlit's own chrome so the page is the only thing on screen.
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .stAppHeader {display: none;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      [data-testid="stAppViewContainer"] > .main {padding: 0 !important;}
      iframe {display: block; margin: 0 auto;}
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "index.html"

if not html_path.exists():
    st.error("index.html not found next to app.py.")
    st.stop()

components.html(
    html_path.read_text(encoding="utf-8"),
    height=PAGE_HEIGHT,
    scrolling=False,
)
