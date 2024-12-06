from src.llm_interface import query_llm

def test_query_llm():
    prompt = "What is the hierarchy of openBIS?"
    response = query_llm(prompt)
    assert "hierarchy" in response.lower(), "LLM failed to answer correctly"