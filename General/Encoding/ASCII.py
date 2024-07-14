# Lista de números enteros
numeros = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125];

# Convertir los números a caracteres ASCII y unirlos en una cadena
flag = ''.join(chr(numero) for numero in numeros);

# Imprimir la flag
print("=================== Flag ===================");
print(flag);
