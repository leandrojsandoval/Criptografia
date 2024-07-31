from Crypto.Util.number import long_to_bytes, inverse

# Leer el archivo output.txt
with open('outputManyprime.txt', 'r') as file:
    data = file.read()

# Extraer los valores de n, e y ct
lines = data.split('\n')
n = int(lines[0].split(' = ')[1])
e = int(lines[1].split(' = ')[1])
ct = int(lines[2].split(' = ')[1])

# Nota estos factores primos obtenidos fueron gracias a la pagina
# https://factordb.com/
# Y aca agregamos el n del archivo de texto

# Lista de factores primos obtenidos
primes = [
    9282105380008121879,
    9303850685953812323,
    9389357739583927789,
    10336650220878499841,
    10638241655447339831,
    11282698189561966721,
    11328768673634243077,
    11403460639036243901,
    11473665579512371723,
    11492065299277279799,
    11530534813954192171,
    11665347949879312361,
    12132158321859677597,
    12834461276877415051,
    12955403765595949597,
    12973972336777979701,
    13099895578757581201,
    13572286589428162097,
    14100640260554622013,
    14178869592193599187,
    14278240802299816541,
    14523070016044624039,
    14963354250199553339,
    15364597561881860737,
    15669758663523555763,
    15824122791679574573,
    15998365463074268941,
    16656402470578844539,
    16898740504023346457,
    17138336856793050757,
    17174065872156629921,
    17281246625998849649
]

# Calcular phi(n)
phi = 1
for p in primes:
    phi *= p - 1

# Calcular d
d = inverse(e, phi)

# Descifrar el mensaje
m = pow(ct, d, n)
print(long_to_bytes(m))
