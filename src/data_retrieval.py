from pybis import Openbis
from config.settings import OPENBIS_URL, OPENBIS_USERNAME, OPENBIS_PASSWORD

# Connect to openBIS
o = Openbis(OPENBIS_URL)
o.login(OPENBIS_USERNAME, OPENBIS_PASSWORD)

def handle_openbis_query(parsed_response):
    if parsed_response["intent"] == "list_projects":
        space_name = parsed_response.get("space")
        if not space_name:
            return "Error: No space specified in the query."
        
        # Fetch projects
        projects = o.get_projects(space=space_name)
        project_list = [project["code"] for project in projects]
        return f"Projects under {space_name}: {', '.join(project_list)}"
    
    return "Sorry, I couldn't understand your query."