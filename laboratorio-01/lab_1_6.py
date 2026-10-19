#Paso 6: validar la blockchain
def validar_blockchain(cadena):
    for posicion, bloque in enumerate(cadena):
        contenido = (
            f"{bloque['indice']}|"
            f"{bloque['datos']}|"
            f"{bloque['hash_anterior']}|"
            f"{bloque['nonce']}"
        )

        hash_recalculado = calcular_hash(contenido)

        if bloque["hash"] != hash_recalculado:
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
                    "no está conectado correctamente con el bloque anterior."
                )
                return False

    return True