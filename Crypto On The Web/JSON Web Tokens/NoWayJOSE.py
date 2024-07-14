import base64;
import json;

# Header
header = json.dumps({"typ": "JWT", "alg": "none"}).encode();
header_b64 = base64.urlsafe_b64encode(header).decode().rstrip('=');

# Payload
payload = json.dumps({"admin": True}).encode();
payload_b64 = base64.urlsafe_b64encode(payload).decode().rstrip('=');

# JWT
jwt_token = f"{header_b64}.{payload_b64}.";
print("Token Manipulado (Ingresar este token en la siguiente url : https://web.cryptohack.org/no-way-jose/)");
print(jwt_token);
