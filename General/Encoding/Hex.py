# Para decodificar la cadena hexadecimal y obtener la flag original
# 1 - Convierte la cadena hexadecimal a bytes usando bytes.fromhex().
# 2 - Decodifica los bytes a una cadena ASCII usando .decode('ASCII').

# Cadena hexadecimal proporcionada
hex_string = "63727970746f7b596f755f77696e5f7468655f6865785f737472696e675f625f6361726566756c7d";

# Convertir la cadena hexadecimal a bytes
mensajeBytes = bytes.fromhex(hex_string);

# Decodificar los bytes a una cadena ASCII
flag = mensajeBytes.decode('ASCII');

# Imprimir el mensaje
print("=================== Flag ===================");
print(flag);
