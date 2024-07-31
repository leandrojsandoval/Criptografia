import hashlib
from Crypto.Util.number import bytes_to_long

# Función para cargar N y d desde el archivo private.key
def load_private_key(filename):
    params = {}
    with open(filename, 'r') as f:
        for line in f:
            key, value = line.strip().split(' = ')
            params[key] = int(value)
    return params['N'], params['d']

# Función para firmar un mensaje usando RSA con la clave privada
def sign_message(message, N, d):
    # Calcular el hash SHA256 del mensaje
    hash_object = hashlib.sha256(message.encode())
    hash_digest = hash_object.digest()

    # Convertir el hash en un número
    hash_num = bytes_to_long(hash_digest)

    # Firmar el mensaje utilizando RSA
    signature = pow(hash_num, d, N)

    return signature

# Nombre del archivo private.key
private_key_file = 'private.key'

# Cargar N y d desde el archivo private.key
N, d = load_private_key(private_key_file)

# Mensaje a firmar
message = "crypto{Immut4ble_m3ssag1ng}"

# Obtener la firma digital
signature = sign_message(message, N, d)

# Imprimir la firma resultante
print("Firma digital:", signature)
