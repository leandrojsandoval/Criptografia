# Definimos las claves y resultados en formato hexadecimal
KEY1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313";
KEY2_XOR_KEY1_hex = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e";
KEY2_XOR_KEY3_hex = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1";
FLAG_XOR_KEYS_hex = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf";

# Convertimos de hexadecimal a bytes
KEY1 = bytes.fromhex(KEY1_hex);
KEY2_XOR_KEY1 = bytes.fromhex(KEY2_XOR_KEY1_hex);
KEY2_XOR_KEY3 = bytes.fromhex(KEY2_XOR_KEY3_hex);
FLAG_XOR_KEYS = bytes.fromhex(FLAG_XOR_KEYS_hex);

# Calculamos KEY2, KEY3 y finalmente el FLAG original
KEY2 = bytes(a ^ b for a, b in zip(KEY2_XOR_KEY1, KEY1));
KEY3 = bytes(a ^ b for a, b in zip(KEY2_XOR_KEY3, KEY2));
FLAG = bytes(a ^ b ^ c ^ d for a, b, c, d in zip(FLAG_XOR_KEYS, KEY1, KEY3, KEY2));

# Convertimos el resultado final a texto
flag_text = FLAG.decode('utf-8');

# Imprimimos el resultado final
print("=================== Flag ===================");
print(flag_text);
