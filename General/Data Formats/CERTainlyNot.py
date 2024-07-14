from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509 import load_der_x509_certificate

def extract_modulus_from_certificate(der_file):
    with open(der_file, "rb") as f:
        cert_data = f.read()
    
    cert = load_der_x509_certificate(cert_data, default_backend())
    public_key = cert.public_key()
    rsa_public_key = public_key.public_numbers()
    
    modulus = rsa_public_key.n
    return modulus

# Replace with the path to your DER-encoded certificate file
der_file = "2048b-rsa-example-cert.der";

modulus = extract_modulus_from_certificate(der_file);
print("=================== Modulo ===================");
print(modulus);
