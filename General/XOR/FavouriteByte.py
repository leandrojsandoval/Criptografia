# Cadena cifrada en hexadecimal
hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d";

# Convertir de hexadecimal a bytes
cipher_bytes = bytes.fromhex(hex_string);

# Probamos todas las combinaciones posibles de un byte (0x00 a 0xFF)
for clave in range(256):
    # Generamos una lista de bytes obtenidos al aplicar XOR con la clave actual
    bytesDesencriptados = bytes(c ^ clave for c in cipher_bytes);
    
    # Verificamos si el resultado descifrado contiene la palabra "crypto"
    if b'crypto' in bytesDesencriptados:
        # Convertimos los bytes decifrados a texto
        flag = bytesDesencriptados.decode('utf-8');
        print(f"Clave encontrada: {clave}");
        print("=================== Flag ===================");
        print(flag);
        break
