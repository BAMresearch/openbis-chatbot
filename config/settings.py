from decouple import config

# Cargar las variables desde .env
username = config("OPENBIS_USERNAME")
password = config("OPENBIS_PASSWORD")
url = config("OPENBIS_URL")

#username = config("OPENBIS_USERNAME", default="default_username") --> default values

# Usar las variables en tu aplicación
print(f"Username: {username}")
print(f"Connecting to OpenBIS at {url}")