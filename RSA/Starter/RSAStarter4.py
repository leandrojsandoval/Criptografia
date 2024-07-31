from Crypto.Util.number import inverse

# Definir los valores dados
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

# Calcular el Totiente de Euler φ(N)
phi_N = (p - 1) * (q - 1)

# Calcular la clave privada d usando la función de inversión modular
d = inverse(e, phi_N)

# Imprimir el resultado
print("Clave privada d:", d)
