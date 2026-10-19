#Paso 4: representar manualmente un bloque
import hashlib


def calcular_hash(texto):
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def crear_bloque(indice, datos, hash_anterior, nonce=0):
    contenido = f"{indice}|{datos}|{hash_anterior}|{nonce}"
    hash_actual = calcular_hash(contenido)

    bloque = {
        "indice": indice,
        "datos": datos,
        "hash_anterior": hash_anterior,
        "nonce": nonce,
        "hash": hash_actual
    }

    return bloque


bloque_1 = crear_bloque(
    indice=1,
    datos="Se crean 100 tokens",
    hash_anterior="0" * 64
)

print("BLOQUE GÉNESIS")
print("Número:", bloque_1["indice"])
print("Datos:", bloque_1["datos"])
print("Hash anterior:", bloque_1["hash_anterior"])
print("Nonce:", bloque_1["nonce"])
print("Hash actual:", bloque_1["hash"])