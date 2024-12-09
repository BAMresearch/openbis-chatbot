# **openBIS Chatbot**

A conversational chatbot for querying and retrieving data from openBIS instances using a Large Language Model (LLM). This chatbot allows users to interact with openBIS via natural language, making it easier to explore spaces, projects, experiments, and datasets.

---

## **Features**
- Natural language understanding using Llama 3.2.
- Integration with openBIS API for real-time data retrieval.
- Modular design for easy maintenance and scalability.
- Handles complex queries and provides friendly, human-like responses.
- Error handling for ambiguous or incomplete queries.
- Secure connection to openBIS with robust authentication.

---

## **Getting Started**

### Prerequisites
- Python 3.8 or later.
- A functional openBIS instance.
- Access to the Llama 3.2 model via Ollama.
- `conda` or `pip` installed on your system.

---

### **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/openbis-chatbot.git
   cd openbis-chatbot
   ```

2. Set up a virtual environment (recommended):
   ```bash
   conda create -n chatbot python=3.8
   conda activate chatbot
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up configuration:
   - Edit `config/settings.py` to include your openBIS URL, username, and password.

---

### **Usage**

1. **Run the Chatbot:**
   ```bash
   python src/openbis_chatbot/main.py
   ```

2. **Interact with the Chatbot:**
   - Example Queries:
     - "List all projects under the space 'MY_SPACE'."
     - "What datasets are available in 'Project A'?"
     - "Give me all experiments under 'Space X'."

3. **Exit the Chatbot:**
   - Type `exit` to close the chatbot.

---

## **File Structure**
```
openbis-chatbot/
├── .vscode/
│   └── settings.json
├── examples/
│   ├── example_input.json
│   └── example_output.json
├── src/
│   └── openbis_chatbot/
│       ├── utils/
│       │   ├── logger.py
│       │   └── validators.py
│       ├── prompts/
│       │   ├── base_prompt.txt
│       │   └── examples.txt
│       ├── __init__.py
│       ├── main.py
│       ├── data_retrieval.py
│       ├── llm_interface.py
│       ├── parser.py
│       └── prompt.py
├── tests/
│   ├── data/
│   │   └── # here you can put the files in examples/
│   ├── __init__.py
│   ├── test.py
│   ├── test_data_retrieval.py
│   ├── test_llm_interface.py
│   ├── test_parser.py
│   └── test_prompt.py
├── .gitignore
├── README.md
└── pyproject.toml
```

---

## **How It Works**

1. **User Input**:
   - The user provides a natural language query.
   - Example: "List all projects under 'MY_SPACE'."

2. **LLM Interpretation**:
   - The LLM interprets the query and provides structured intent and entities.
   - Output: `{"intent": "list_projects", "space": "MY_SPACE"}`

3. **Query Parsing**:
   - The query parser validates and extracts the intent and entities.

4. **Data Retrieval**:
   - The system uses openBIS APIs to fetch relevant data.

5. **Response Generation**:
   - The chatbot formats the data into a friendly response and displays it to the user.

---

## **Testing**

To ensure the chatbot is functioning correctly, run the tests:

```bash
pytest tests/
```

---

## **Dependencies**

- `pybis`: Library for interacting with openBIS.
- `ollama-python`: Python client for the Llama model.
- `httpx`: HTTP library for making API requests.

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## **Known Issues**

- Ambiguous queries may require follow-up questions for clarification.
- Large datasets may take longer to process.

---

## **Future Improvements**

1. Add support for more openBIS operations (e.g., creating projects, deleting datasets).
2. Enhance the LLM prompt for better context understanding.
3. Integrate with communication platforms like Slack or Teams.

---

## **Contributing**

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push:
   ```bash
   git commit -m "Add feature name"
   git push origin feature-name
   ```
4. Submit a pull request.

---

## **License**

This project is licensed under the MIT License.

---

## **Contact**

For questions or support, reach out to:
- **Name**: Carlos Madariaga
- **Email**: carlosmadariagaaramendi@gmail.com
- **GitHub**: [Carlos Madariaga Github](https://github.com/carlosmada22)
