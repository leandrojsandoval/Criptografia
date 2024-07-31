from factordb.factordb import FactorDB
from Crypto.Util.number import long_to_bytes

# Datos proporcionados
n = 171731371218065444125482536302245915415603318380280392385291836472299752747934607246477508507827284075763910264995326010251268493630501989810855418416643352631102434317900028697993224868629935657273062472544675693365930943308086634291936846505861203914449338007760990051788980485462592823446469606824421932591                                                                  
e = 65537
ct = 161367550346730604451454756189028938964941280347662098798775466019463375610700074840105776873791605070092554650190486030367121011578171525759600774739890458414593857709994072516290998135846956596662071379067305011746842247628316996977338024343628757374524136260758515864509435302781735938531030576289086798942  

# Función para obtener los factores primos de n usando FactorDB
def factorize(n):
    f = FactorDB(n)
    f.connect()
    f.get_factor_list()
    return f.get_factor_list()

# Obtener los factores primos de n
factors = factorize(n)
print("Factores encontrados:", factors)

# Verificar que hay exactamente dos factores
if len(factors) != 2:
    print("No se encontraron exactamente dos factores primos.")
    exit()

# Asignar p y q
p, q = factors

# Calcular phi y d
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)  # Calcular el inverso modular de e módulo phi

# Descifrar el mensaje
pt = pow(ct, d, n)
plaintext = long_to_bytes(pt)
print("Mensaje descifrado:", plaintext.decode())
