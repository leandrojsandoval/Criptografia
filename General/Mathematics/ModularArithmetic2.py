# Utilizando el Teorema Pequeño de Fermat
p = 65537;
a = 27324678765465536;

flag = a**(p-1) % p;
print("=================== Flag ===================");
print(flag);
