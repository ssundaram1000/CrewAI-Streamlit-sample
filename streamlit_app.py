import streamlit as st
from pathlib import Path

import sys
try:
    __import__('pysqlite3')
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ModuleNotFoundError:
    # We're on macOS (no wheel) or the wheel failed to install.
    # Either fall back to the real sqlite3, or leave your stub in place.
    pass

# make src/ importable
sys.path.append(str(Path(__file__).parent / "src"))

from quick_research.main import run_topic

st.set_page_config(page_title="CrewAI Demo", page_icon="🤖")
st.title("🤖 CrewAI + Streamlit")

if "chat" not in st.session_state: st.session_state.chat = []

for role, txt in st.session_state.chat:
    st.chat_message(role).markdown(txt)

prompt = st.chat_input("What topic do you want me to research…")
if prompt:
    st.chat_message("user").markdown(prompt)
    with st.spinner("Thinking…"):
        answer = run_topic(prompt)
    st.chat_message("assistant").markdown(answer)
    st.session_state.chat.append(("user", prompt))
    st.session_state.chat.append(("assistant", answer))
