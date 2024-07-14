# Para resolver este problema, se debe convertir la cadena hexadecimal en bytes utilizando la 
# función bytes.fromhex(). Luego, podemos usar la función base64.b64encode() del módulo base64 
# para codificar esos bytes en Base64.

import base64;

hexString = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf";

# Convertir la cadena hexadecimal a bytes
bytesData = bytes.fromhex(hexString);

# Codificar los bytes en Base64
base64Encoded = base64.b64encode(bytesData);

# Imprimir la representación en Base64
print("=================== Flag ===================");
print(base64Encoded.decode('ASCII'));
