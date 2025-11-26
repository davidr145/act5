import random
import time
resultados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
inicio = time.time()
while time.time() - inicio < 3:
    dado = random.randint(1, 6)
    resultados[dado] += 1
print(f"RESUMEN Tiempo: {time.time() - inicio}")
for numero, cantidad in resultados.items():
    print(f"{numero}: {cantidad}")