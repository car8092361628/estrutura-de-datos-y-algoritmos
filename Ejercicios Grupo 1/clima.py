import requests

# URL de la API del clima con una ciudad específica (ejemplo: Santo Domingo)
url = "https://api.weatherapi.com/v1/current.json?key=TU_CLAVE&q=Santo Domingo"

try:
    # Hacer la solicitud GET
    respuesta = requests.get(url)
    respuesta.raise_for_status()  # Verificar si hubo un error HTTP

    # Convertir la respuesta a JSON
    datos = respuesta.json()

    # Validar si los datos esperados están presentes
    if "location" in datos and "current" in datos:
        ciudad = datos["location"]["name"]
        temperatura = datos["current"]["temp_c"]
        condicion = datos["current"]["condition"]["text"]

        print(f"🌤 Clima en {ciudad}: {temperatura}°C, {condicion}")
    else:
        print("Error: La respuesta de la API no contiene los datos esperados.")

except requests.exceptions.RequestException as e:
    print(f"Error al realizar la solicitud: {e}")
except KeyError as e:
    print(f"Error al acceder a los datos: {e}")