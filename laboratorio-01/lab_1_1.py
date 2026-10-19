##Construcción manual de una blockchain

import hashlib


texto = "Fernando envía 10 USDT a María"

hash_resultado = hashlib.sha256(texto.encode("utf-8")).hexdigest()


print("Texto original:")
print(texto)


print("\nHash SHA-256:")
print(hash_resultado)