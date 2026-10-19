
#Paso 5: construir una cadena de cuatro bloques
import hashlib
import hashlib


def calcular_hash(texto):
    """Calcula el hash SHA-256 de un texto."""
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def calcular_hash_bloque(bloque):
    """Recalcula el hash usando el contenido de un bloque."""
    contenido = (
        f"{bloque['indice']}|"
        f"{bloque['datos']}|"
        f"{bloque['hash_anterior']}|"
        f"{bloque['nonce']}"
    )

    return calcular_hash(contenido)


def crear_bloque(indice, datos, hash_anterior, nonce=0):
    """Crea un nuevo bloque."""
    bloque = {
        "indice": indice,
        "datos": datos,
        "hash_anterior": hash_anterior,
        "nonce": nonce
    }

    bloque["hash"] = calcular_hash_bloque(bloque)

    return bloque


def mostrar_blockchain(cadena):
    """Muestra todos los bloques."""
    for bloque in cadena:
        print("\n" + "=" * 70)
        print(f"BLOQUE {bloque['indice']}")
        print("=" * 70)
        print("Datos:", bloque["datos"])
        print("Hash anterior:", bloque["hash_anterior"])
        print("Nonce:", bloque["nonce"])
        print("Hash actual:", bloque["hash"])


def validar_blockchain(cadena):
    """Comprueba la integridad y los enlaces de la cadena."""
    for posicion, bloque in enumerate(cadena):
        hash_recalculado = calcular_hash_bloque(bloque)

        if bloque["hash"] != hash_recalculado:
            print(f"hash bloque 2: {bloque['hash']}")
            print(f"hash bloque 2 recalculado: {hash_recalculado}")
            print(
                f"Bloque {bloque['indice']} inválido: "
                "sus datos no coinciden con su hash."
            )
            return False

        if posicion > 0:
            bloque_anterior = cadena[posicion - 1]

            if bloque["hash_anterior"] != bloque_anterior["hash"]:
                print(
                    f"Bloque {bloque['indice']} inválido: "
                    "su hash anterior no coincide."
                )
                return False

    return True


def reconstruir_desde(cadena, posicion_inicial):
    """Reconstruye los hashes desde una posición determinada."""
    for posicion in range(posicion_inicial, len(cadena)):
        bloque = cadena[posicion]

        if posicion > 0:
            bloque["hash_anterior"] = cadena[posicion - 1]["hash"]

        bloque["hash"] = calcular_hash_bloque(bloque)


# 1. Construcción de la blockchain
bloque_1 = crear_bloque(
    1,
    "Se crean 100 tokens",
    "0" * 64
)

bloque_2 = crear_bloque(
    2,
    "Ana envía 20 tokens a Luis",
    bloque_1["hash"]
)

bloque_3 = crear_bloque(
    3,
    "Luis envía 5 tokens a Carla",
    bloque_2["hash"]
)

bloque_4 = crear_bloque(
    4,
    "Carla envía 2 tokens a Pedro",
    bloque_3["hash"]
)

blockchain = [
    bloque_1,
    bloque_2,
    bloque_3,
    bloque_4
]

# 2. Mostrar y validar la cadena original
# print("\nBLOCKCHAIN ORIGINAL")
# mostrar_blockchain(blockchain)

# print("\n¿La cadena es válida?")
# print(validar_blockchain(blockchain))

# 3. Alterar los datos del bloque 2
print("\nALTERACIÓN DEL BLOQUE 2")
blockchain[1]["datos"] = "Ana envía 80 tokens a Luis"

print("\n¿La cadena sigue siendo válida?")
print(validar_blockchain(blockchain))

# 4. Recalcular solamente el hash del bloque 2
print("\nRECALCULANDO SOLAMENTE EL BLOQUE 2")
blockchain[1]["hash"] = calcular_hash_bloque(blockchain[1])

print("\n¿La cadena es válida?")
print(validar_blockchain(blockchain))

# 5. Reconstruir todos los bloques posteriores
print("\nRECONSTRUYENDO LA CADENA DESDE EL BLOQUE 2")
reconstruir_desde(blockchain, 1)

# mostrar_blockchain(blockchain)

print("\n¿La cadena reconstruida es válida?")
print(validar_blockchain(blockchain))