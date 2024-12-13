from ollama import Client
from config.settings import LLM_MODEL

def query_llm(prompt):
    client = Client()
    raw_response = client.generate(model="llama3.2", prompt=prompt)
    
    try:
        response = LLMResponse.parse_raw(raw_response)
        return response
    except ValidationError as e:
        raise ValueError(f"Invalid LLM response: {e}")