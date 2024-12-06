def generate_prompt(user_query):
    with open("prompts/base_prompt.txt", "r") as file:
        base_prompt = file.read()
    return f"{base_prompt}\n\nUser Query: \"{user_query}\""