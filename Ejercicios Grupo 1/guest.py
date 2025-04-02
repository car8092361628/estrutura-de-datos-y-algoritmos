import requests

def get_weather(api_key, lat=33.44, lon=-94.04):
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si la respuesta tiene error
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return None

if __name__ == "__main__":
    API_KEY = "32b1941c850885b32501f0eb624465b0"  # Reemplaza con tu clave de API de OpenWeatherMap
    weather_data = get_weather(API_KEY)
    if weather_data:
        print(weather_data)
