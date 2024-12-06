from src.parser import parse_llm_response

def test_parse_llm_response():
    response = '{"intent": "list_projects", "space": "MY_SPACE"}'
    parsed = parse_llm_response(response)
    assert parsed["intent"] == "list_projects", "Parser failed to extract intent"
    assert parsed["space"] == "MY_SPACE", "Parser failed to extract space"