def validate_parsed_response(parsed_response):
    """
    Validate the parsed LLM response to ensure it contains the required fields.
    """
    required_keys = ["intent"]
    if parsed_response["intent"] == "list_projects":
        required_keys.append("space")

    missing_keys = [key for key in required_keys if key not in parsed_response]
    if missing_keys:
        return False, f"Missing required keys: {', '.join(missing_keys)}"
    return True, None

def validate_user_query(user_query):
    """
    Validate the user's query to ensure it's a non-empty string.
    """
    if not isinstance(user_query, str) or not user_query.strip():
        return False, "Invalid query: Query must be a non-empty string."
    return True, None
