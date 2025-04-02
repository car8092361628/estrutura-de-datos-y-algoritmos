import requests

API_KEY = "78959aa7029348e97f6fc2ffd0af91ac"  # Tu clave de API aquí
lat = 33.44
lon = -94.04
url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEY}"

response = requests.get(url)
print(response.status_code)  # Esto imprimirá el código de estado de la respuesta
print(response.text)  # Esto imprimirá el contenido de la respuesta