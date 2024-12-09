import json

def parse_llm_response(response):
    """
    Parse LLM response to extract intent and entities.
    Expected response: {"intent": "list_projects", "space": "MY_SPACE"}
    """
    try:
        parsed_response = json.loads(response)
        return parsed_response
    except json.JSONDecodeError:
        return {"intent": "unknown", "error": "Invalid LLM response format"}