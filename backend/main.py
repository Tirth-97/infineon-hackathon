from langchain_community.llms import Ollama

llm = Ollama(model="phi3")

response = llm.invoke("Explain what Infineon does in 2 lines")
print(response)
