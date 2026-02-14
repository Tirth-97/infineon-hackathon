BUG_ANALYSIS_PROMPT = """
You are an expert Python debugging assistant.

Given this Python code and error (if any):
----------------
{code}
----------------
Error:
{error}

1. Identify the bug type (syntax / runtime / logic).
2. Explain the root cause in simple words.
3. Point out the exact line or function.
4. Suggest a fix.
5. Provide corrected code snippet.
"""
