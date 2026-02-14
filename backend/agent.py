from llm import ask_llm
from prompts import BUG_ANALYSIS_PROMPT

class BugHunterAgent:
    def __init__(self):
        pass

    def analyze(self, code: str, error: str):
        prompt = BUG_ANALYSIS_PROMPT.format(code=code, error=error)

        print("🧠 Agent: Thinking about the bug...")
        response = ask_llm(prompt)

        return response
