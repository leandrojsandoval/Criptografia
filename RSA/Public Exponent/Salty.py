#!/usr/bin/env python3

# Leer el archivo outputSalty.txt
with open('outputSalty.txt', 'r') as file:
    data = file.read();

# Extraer los valores de n, e y ct
lines = data.split('\n');
n = int(lines[0].split(' = ')[1]);
e = int(lines[1].split(' = ')[1]);
ct = int(lines[2].split(' = ')[1]);

# Convertir el número cifrado (ct) a una cadena hexadecimal
hexed_ct = hex(ct);

# Eliminar el prefijo "0x" y convertir a bytes, luego decodificar a texto
flag = bytearray.fromhex(hexed_ct[2:]).decode();

# Imprimir el mensaje descifrado
print("=================== Flag ===================");
print(flag);
