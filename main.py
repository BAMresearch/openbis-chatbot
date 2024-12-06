from src.prompt import generate_prompt
from src.llm_interface import query_llm
from src.parser import parse_llm_response
from src.data_retrieval import handle_openbis_query

def main():
    print("Welcome to the openBIS Chatbot!")
    while True:
        user_query = input("Ask your question (or type 'exit' to quit): ")
        if user_query.lower() == "exit":
            print("Goodbye!")
            break
        
        # Generate prompt
        prompt = generate_prompt(user_query)
        
        # Query the LLM
        llm_response = query_llm(prompt)
        
        # Parse the response
        parsed_response = parse_llm_response(llm_response)
        
        # Handle the query
        final_response = handle_openbis_query(parsed_response)
        
        # Print the result
        print(final_response)

if __name__ == "__main__":
    main()