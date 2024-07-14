# Solución al desafío de Transparencia de cryptohack.org
# Este script utiliza únicamente la base de datos de transparencia de certificados crt.sh
# El script imprimirá la bandera sin intervención manual del usuario

"""
Pasos:
  1) Obtener el hash SHA-256 del DER de la clave pública del sujeto
  2) Buscar este valor en crt.sh, lo cual nos proporcionará el certificado que tiene este SPKI
  3) Obtener el certificado PEM y analizar su contenido para obtener el atributo commonName (nombre común)
  4) Consultar el nombre común y obtener la bandera
"""

from Crypto.PublicKey import RSA;
from OpenSSL.crypto import load_certificate, FILETYPE_PEM;
import hashlib;
import json;
import requests;

## 1) Obtener el hash SHA-256 de la clave pública DER
# Abrir el archivo PEM proporcionado
archivoPEM = open("transparency.pem", "r").read();
claveRSA = RSA.importKey(archivoPEM).public_key();
# Convertir el PEM a formato DER para obtener el hash
der = claveRSA.exportKey(format='DER');
# Obtener el hash SHA-256 de la clave pública DER, que usaremos en crt.sh
digest = hashlib.sha256(der).hexdigest();

## 2) Buscar el certificado que tenga este SPKI específico
# Encabezado para las solicitudes HTTP
agente_usuario = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1';
# URL de búsqueda en crt.sh por SPKI
url_spki = "https://crt.sh/?spkisha256={hash}&output=json";
# El parámetro output=json indica a crt.sh que devuelva datos en formato JSON en lugar de HTML
respuesta = requests.get(url_spki.format(hash=digest), headers={'User-Agent': agente_usuario});
contenido = respuesta.content.decode('utf-8');
datos = json.loads(contenido);
# Obtener el ID del certificado con ese SPKI específico
idCertificado = datos[0]["id"];

# URL de descarga del certificado PEM desde crt.sh
urlDescarga = "https://crt.sh/?d={id}";
respuesta = requests.get(urlDescarga.format(id=idCertificado), headers={'User-Agent': agente_usuario});
# Este es el certificado PEM que contiene ese SPKI específico
certificadoPEM = respuesta.content.decode('utf-8');

## 3) Obtener el campo del Nombre Común (commonName):
# Devuelve un objeto X.509
certificado = load_certificate(FILETYPE_PEM, certificadoPEM);
# Obtener el Nombre Común del sujeto del certificado
nombre_comun = certificado.get_subject().commonName;
# Imprimir el Nombre Común del sujeto
print("El Nombre Común del sujeto del certificado es:", nombre_comun);

## 4) Obtener la bandera:
urlFlag = "https://" + nombre_comun;
respuesta = requests.get(urlFlag, headers={'User-Agent': agente_usuario});
flag = respuesta.content.decode('utf-8');
print("=================== Flag ===================");
print(flag);
