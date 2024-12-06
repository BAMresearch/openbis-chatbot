from src.data_retrieval import handle_openbis_query

def test_handle_openbis_query():
    parsed_response = {"intent": "list_projects", "space": "MY_SPACE"}
    result = handle_openbis_query(parsed_response)
    assert "Projects under MY_SPACE" in result, "Data retrieval failed"