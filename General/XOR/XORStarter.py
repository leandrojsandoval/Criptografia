def xor_with_13(label):
    new_chars = []
    for char in label:
        # Obtiene el valor Unicode del carácter
        unicode_value = ord(char);
        # Aplica XOR con 13
        xor_value = unicode_value ^ 13;
        # Convierte el valor resultante de nuevo a carácter
        new_char = chr(xor_value);
        # Agrega el nuevo carácter a la lista
        new_chars.append(new_char);
    
    # Une todos los caracteres en una cadena
    new_string = ''.join(new_chars);
    # Formatea el flag final
    flag = f'crypto{{{new_string}}}';
    return flag

# Reemplaza esto con la cadena proporcionada
label = "label";
flag = xor_with_13(label);
print("=================== Flag ===================");
print(flag);
