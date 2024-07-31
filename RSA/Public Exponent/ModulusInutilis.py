#!/usr/bin/env python3

import gmpy2
from Crypto.Util.number import long_to_bytes

# Leer el archivo outputModulusInutilis.txt
with open('outputModulusInutilis.txt', 'r') as file:
    data = file.read();

# Extraer los valores de n, e y ct
lines = data.split('\n')
n = int(lines[0].split(' = ')[1]);
e = int(lines[1].split(' = ')[1]);
ct = int(lines[2].split(' = ')[1]);

# Calcular la raíz cúbica de ct
m = gmpy2.iroot(ct, e)[0];

# Convertir el mensaje descifrado a bytes
flag = long_to_bytes(m);

# Imprimir el mensaje descifrado
print("=================== Flag ===================");
print(flag);
