
import hashlib


def calcular_hash(texto):
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


texto_original = "Fernando envía 10 USDT a María"
texto_modificado = "Fernando envía 20 USDT a María"

print("Hash original:")
print(calcular_hash(texto_original))

print("\nHash modificado:")
print(calcular_hash(texto_modificado))