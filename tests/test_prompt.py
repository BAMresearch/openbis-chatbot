from src.prompt import generate_prompt
from ollama import Client

client = Client()
query = "Give me all projects under the space 'MY_SPACE'."
prompt = generate_prompt(query)
response = client.generate(model="llama3.2", prompt=prompt)
print(response)