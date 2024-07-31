from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes, GCD
from factordb.factordb import FactorDB  # Importar desde Factordb.
import re

# Valores de output.txt
n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373

# Factorización de n
# Usar FactorDB o el módulo factordb para factorizar n
fdb = FactorDB(n)
fdb.connect()
if not fdb.get_factor_list():
    fdb.gmp_factor(n)
p, q = fdb.get_factor_list()

# Calcular phi y la clave privada d
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

# Descifrar el mensaje cifrado
pt = pow(ct, d, n)
decrypted = long_to_bytes(pt).decode()

# Imprimir el resultado
print(f"Mensaje descifrado: {decrypted}")

# Extraer el flag de la salida
flag_match = re.search(r'crypto\{(.+?)\}', decrypted)
if flag_match:
    flag = flag_match.group(1)
    print(f"Flag: crypto{{{flag}}}")
else:
    print("No se encontró el formato del flag en el mensaje descifrado.")
