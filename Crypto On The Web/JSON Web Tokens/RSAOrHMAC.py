# PARA QUE SE EJECUTE EL SCRIPT CORRECTAMENTE HAY QUE HACER LO SIGUIENTE
#
# 1 - Ejecutar el comando pip show pyjwt en la terminal e irte a la ubicacion de las librerias
# Ejemplo: C:\Users\leand\AppData\Local\Programs\Python\Python312\Lib\site-packages
#
# 2 - Irte a la carpeta jwt y al archivo algoritms.py
#
# 3 - Buscar las funciones que tengan como firma prepare_key de nombre
#
# 4 - Comentar en sus funciones todo lo relacionado a InvalidKeyError
# Existen algunas que se encuentran dentro de un bloque if o else (comentar el bloque)
#
# La salida deberia figurar de la siguiente manera:
#
# D:\UNLAM\Criptografia\Trabajos Practicos\Trabajo Práctico 4\JSON Web Tokens>py RSAOrHMAC.py
# Public Key:
# -----BEGIN RSA PUBLIC KEY-----
# MIIBCgKCAQEAvoOtsfF5Gtkr2Swy0xzuUp5J3w8bJY5oF7TgDrkAhg1sFUEaCMlR
# YltE8jobFTyPo5cciBHD7huZVHLtRqdhkmPD4FSlKaaX2DfzqyiZaPhZZT62w7Hi
# gJlwG7M0xTUljQ6WBiIFW9By3amqYxyR2rOq8Y68ewN000VSFXy7FZjQ/CDA3wSl
# Q4KI40YEHBNeCl6QWXWxBb8AvHo4lkJ5zZyNje+uxq8St1WlZ8/5v55eavshcfD1
# 0NSHaYIIilh9yic/xK4t20qvyZKe6Gpdw6vTyefw4+Hhp1gROwOrIa0X0alVepg9
# Jddv6V/d/qjDRzpJIop9DSB8qcF1X23pkQIDAQAB
# -----END RSA PUBLIC KEY-----
# Generated Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiYWRtaW4iOnRydWV9.ilYg-wRobcU9pAannICe4ZxmFhfOh1nXcWf8tJ6UyOY
# {'response': 'Welcome admin, here is your flag: crypto{Doom_Principle_Strikes_Again}'}'''

import requests
import jwt

# URL base del desafío
base_url = "https://web.cryptohack.org/rsa-or-hmac/"

# Obtener la clave pública del servidor
response = requests.get(f"{base_url}get_pubkey/")
public_key = response.json()["pubkey"]
print(f"Public Key: {public_key}")

# Crear un token JWT malicioso con algoritmo HS256 usando la clave pública como secreto
payload = {
    "username": "admin",
    "admin": True
}

# Crear el token HS256
token = jwt.encode(payload, public_key, algorithm='HS256')
print(f"Generated Token: {token}")

# Enviar el token al servidor para autorizar y obtener el FLAG
response = requests.get(f"{base_url}authorise/{token}/")
print(response.json())
