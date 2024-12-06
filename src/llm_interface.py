from ollama import Client
from config.settings import LLM_MODEL

def query_llm(prompt):
    client = Client()
    response = client.generate(model=LLM_MODEL, prompt=prompt)
    return response