import requests

respuesta = requests.get("https://api.github.com")  # Solicitud HTTP GET
print("  Código de respuesta:   ", respuesta.status_code)
