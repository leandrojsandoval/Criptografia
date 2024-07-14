import jwt
import requests

# Intentamos con un secret key común
SECRET_KEY = "secret"

# Generar un token JWT con privilegios de administrador
payload = {
    "username": "admin",
    "admin": True
}

# Codificar el token usando el secret key
token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
print(f"Generated token: {token}")

# Una vez que tengas el token, puedes usarlo para hacer una petición a la ruta /jwt-secrets/authorise/

# URL base del desafío
base_url = "https://web.cryptohack.org/jwt-secrets/"

# Hacer una petición a la ruta /authorise/
response = requests.get(f"{base_url}authorise/{token}/")

# Imprimir la respuesta para ver el FLAG
print(response.json())
