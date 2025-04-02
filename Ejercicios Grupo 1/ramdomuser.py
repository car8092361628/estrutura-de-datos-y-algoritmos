import requests

# URL de la API pública (Random User Generator)
url_api = "https://randomuser.me/api/"

# Hacer la solicitud GET
try:
    respuesta = requests.get(url_api)

    # Verificar si la respuesta es exitosa (código 200)
    if respuesta.status_code == 200:
        datos = respuesta.json()  # Convertir la respuesta a JSON
        
        # Extraer información del usuario generado aleatoriamente
        usuario = datos["results"][0]
        nombre = usuario["name"]["first"]
        apellido = usuario["name"]["last"]
        pais = usuario["location"]["country"]
        email = usuario["email"]

        # Mostrar la información obtenida
        print(f"👤 Usuario Generado:")
        print(f"Nombre: {nombre} {apellido}")
        print(f"País: {pais}")
        print(f"Email: {email}")
    else:
        print("❌ Error al obtener los datos.")

except Exception as e:
    print(f"❌ Ocurrió un error: {e}")
