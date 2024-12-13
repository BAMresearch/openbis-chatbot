import json
from pydantic import BaseModel, ValidationError
from typing import Optional

def parse_llm_response(response):
    """
    Parse LLM response to extract intent and entities.
    Expected response: {"intent": "list_projects", "space": "MY_SPACE"}
    """
    intent: str
    space: Optional[str]
    project: Optional[str]
    experiment: Optional[str]
    try:
        parsed_response = json.loads(response)
        return parsed_response
    except json.JSONDecodeError:
        return {"intent": "unknown", "error": "Invalid LLM response format"}