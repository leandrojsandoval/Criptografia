from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def extract_modulus_and_exponent_from_ssh_public_key_file(filename):
    with open(filename, 'rb') as f:
        pubkey = serialization.load_ssh_public_key(f.read(), backend=default_backend());
    
    key_modulus = pubkey.public_numbers().n;
    key_exponent = pubkey.public_numbers().e;
    
    return key_modulus, key_exponent;

# Nombre del archivo que contiene la clave pública SSH
ssh_pubkey_file = "bruce_rsa.pub"

# Extraer el módulo y el exponente
modulus, exponent = extract_modulus_and_exponent_from_ssh_public_key_file(ssh_pubkey_file);

print("=================== Modulo ===================");
print(f"Modulus (n): {modulus}");
print(f"Exponent (e): {exponent}");
