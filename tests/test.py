from ollama import Client
from pybis import Openbis
import getpass

def generate_prompt(client, user_query):
    # Initialize the Ollama client
    openbis_structure = """
    openBIS is a data management system with the following hierarchy:
    - Spaces contain projects.
    - Projects contain experiments.
    - Experiments contain objects.
    - Objects contain datasets (real data)

    Your task is to interpret the query and guide the system to retrieve the correct data.
    """
    prompt = f"{openbis_structure}\n\nUser Query: \"{user_query}\""
    return prompt


# Send a prompt to the model
#response = client.generate(model="llama3.2", prompt="Explain the importance of data organization.")
#print(response)
#pat : $pat-cmadaria-241205170201738x4C4FA330C6E2A477ECDAF3FF1E9B1D4C

#o = Openbis('https://devel.datastore.bam.de/', verify_certificates=False)
#o.login('cmadaria', getpass.getpass(), save_token=True)
#pat = o.get_or_create_personal_access_token('test-session')
#print(pat)

pat = '$pat-cmadaria-241205170201738x4C4FA330C6E2A477ECDAF3FF1E9B1D4C'
o = Openbis(url='https://devel.datastore.bam.de/', token=pat, verify_certificates=False)


# Fetch data from a specific space
data = o.get_spaces()
print(data)

#prompt = f"What can you tell me about the following space in openBIS? {data}"

client = Client()

query = f"Give me all the projects under the space 'CMADARIA' {data}"
prompt = generate_prompt(client, query)
response = client.generate(model="llama3.2", prompt=prompt)
print(response.response)