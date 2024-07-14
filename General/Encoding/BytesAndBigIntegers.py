# Para resolver este problema utilizando PyCryptodome, utilizamos la función long_to_bytes() 
# del módulo Crypto.Util.number. Esta función convierte un número entero largo en una cadena 
# de bytes.

# Este código tomará el número entero integer, lo convertirá en una cadena de bytes utilizando 
# la función long_to_bytes() y luego imprimirá el mensaje resultante.

from Crypto.Util.number import long_to_bytes

integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269;

# Convertir el entero largo en una cadena de bytes
mensajeBytes = long_to_bytes(integer);

# Imprimir el mensaje
print("=================== Flag ===================");
print(mensajeBytes.decode('ASCII'));
