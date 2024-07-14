from Crypto.PublicKey import RSA
import base64

# Nombre del archivo PEM
pem_file = "privacy_enhanced_mail.pem"

# Función para extraer la clave privada d como entero
def extract_private_key(pem_file):
    with open(pem_file, "r") as f:
        pem_data = f.read()

        # Extraer el contenido base64 entre los encabezados y pies de página
        pem_lines = pem_data.split("\n")
        base64_data = ""
        in_data = False

        for line in pem_lines:
            if "BEGIN RSA PRIVATE KEY" in line:
                in_data = True
                continue
            elif "END RSA PRIVATE KEY" in line:
                break
            elif in_data:
                base64_data += line.strip()

        # Decodificar datos base64
        der_data = base64.b64decode(base64_data)

        # Importar la clave RSA
        rsa_key = RSA.import_key(der_data)

        # Extraer la parte privada d de la clave RSA
        d = rsa_key.d

        return d

# Llamar a la función para extraer la clave privada
private_key_d = extract_private_key(pem_file);
print("=================== Clave ===================");
print(private_key_d);
