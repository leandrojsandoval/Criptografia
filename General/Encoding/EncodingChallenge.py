from pwn import *
import json
import base64
import codecs
from Crypto.Util.number import long_to_bytes, bytes_to_long

# Establecer la conexión con el servidor
r = remote('socket.cryptohack.org', 13377, level='debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def decode_base64(encoded):
    decoded = base64.b64decode(encoded).decode()
    return decoded

def decode_hex(encoded):
    decoded = bytes.fromhex(encoded).decode()
    return decoded

def decode_rot13(encoded):
    decoded = codecs.decode(encoded, 'rot_13')
    return decoded

def decode_bigint(encoded):
    decoded = long_to_bytes(int(encoded, 16)).decode()
    return decoded

def decode_utf8(encoded):
    decoded = ''.join(chr(b) for b in encoded)
    return decoded

# Función para manejar cada nivel del desafío
def handle_challenge():
    received = json_recv()
    encoding_type = received["type"]
    encoded_value = received["encoded"]
    
    if encoding_type == "base64":
        decoded_value = decode_base64(encoded_value)
    elif encoding_type == "hex":
        decoded_value = decode_hex(encoded_value)
    elif encoding_type == "rot13":
        decoded_value = decode_rot13(encoded_value)
    elif encoding_type == "bigint":
        decoded_value = decode_bigint(encoded_value)
    elif encoding_type == "utf-8":
        decoded_value = decode_utf8(encoded_value)
    else:
        raise ValueError("Unknown encoding type")

    to_send = {
        "decoded": decoded_value
    }
    
    json_send(to_send)

# Iterar a través de todas las etapas del desafío
for _ in range(100):
    handle_challenge()

# Recibir la bandera final
received_flag = json_recv();
print("=================== Flag ===================");
print(received_flag["flag"]);

# Cerrar la conexión
r.close()
