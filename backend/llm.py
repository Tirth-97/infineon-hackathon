import ollama

def ask_llm(prompt: str):
    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]
