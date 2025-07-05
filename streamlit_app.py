import sys, streamlit as st
from pathlib import Path

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
