# Definir los valores dados
p = 17
q = 23
e = 65537  # Exponente e común en RSA
message = 12

# Calcular N como el producto de p y q
N = p * q

# Calcular el cifrado utilizando RSA
ciphertext = pow(message, e, N)

# Imprimir el resultado
print("Número cifrado:", ciphertext)
