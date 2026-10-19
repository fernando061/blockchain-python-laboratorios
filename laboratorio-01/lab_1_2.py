
import hashlib


texto_original = "Fernando envía 10 USDT a María"
texto_modificado = "Fernando envía 20 USDT a María"

hash_original = hashlib.sha256(
    texto_original.encode("utf-8")
).hexdigest()

hash_modificado = hashlib.sha256(
    texto_modificado.encode("utf-8")
).hexdigest()

print("Texto original:")
print(texto_original)
print(hash_original)

print("\nTexto modificado:")
print(texto_modificado)
print(hash_modificado)

print("\n¿Los hashes son iguales?")
print(hash_original == hash_modificado)