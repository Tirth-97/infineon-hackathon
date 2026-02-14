import streamlit as st
from agent import BugHunterAgent

st.set_page_config(page_title="Agentic Bug Hunter", layout="wide")

st.title("🛠️ Agentic Bug Hunter")
st.write("Paste your Python code below and let the AI agent find and explain bugs.")

# Text area for user to paste code
code_input = st.text_area("🐍 Paste your Python code here:", height=300)

analyze_button = st.button("🔍 Analyze Code")

if analyze_button:
    if not code_input.strip():
        st.warning("Please paste some Python code first.")
    else:
        st.info("🤖 Agent is analyzing your code... Please wait.")

        agent = BugHunterAgent()
        report = agent.analyze(code_input, error="No runtime log provided")

        st.success("✅ Analysis Complete!")

        st.subheader("🛠️ AGENTIC BUG HUNTER REPORT")
        st.markdown("---")

        # For now, show raw AI report
        st.text(report)

        st.markdown("---")
        st.caption("Powered by Agentic AI for Automatic Bug Detection and Explanation")
