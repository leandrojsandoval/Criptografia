from sympy import isprime, mod_inverse
from Crypto.Util.number import long_to_bytes
import binascii

def isqrt(n):
    """Returns the integer square root of n."""
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def factorize_and_compute_phi(n):
    p = isqrt(n)
    assert p * p == n and isprime(p), "n is not a square of a prime number"
    q = p
    phi = (p - 1) * (q - 1)
    return p, q, phi

def decrypt_rsa(ct, d, n):
    return pow(ct, d, n)

# Leer el archivo de salida
with open('outputSquareEyes.txt', 'r') as file:
    lines = file.readlines()
    n = int(lines[0].split('=')[1].strip())
    e = int(lines[1].split('=')[1].strip())
    ct = int(lines[2].split('=')[1].strip())

# Calcular los factores y phi
p, q, phi = factorize_and_compute_phi(n)
print(f"p = {p}")
print(f"q = {q}")
print(f"phi = {phi}")

# Calcular la clave privada d
d = mod_inverse(e, phi)
print(f"d = {d}")

# Desencriptar el mensaje
decrypted_message = decrypt_rsa(ct, d, n)
print(f"Decrypted message (as integer): {decrypted_message}")

# Convertir el mensaje desencriptado de entero a bytes
decrypted_bytes = long_to_bytes(decrypted_message)
print(f"Decrypted message (as bytes): {decrypted_bytes}")

# Assuming decrypted_bytes contains the bytes from decryption
flag = binascii.hexlify(decrypted_bytes).decode('utf-8')

# Convertir los bytes a cadena
#flag = decrypted_bytes.decode('utf-8')
print(f"Flag: {flag}")




