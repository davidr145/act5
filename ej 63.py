import random
resultados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for _ in range(100):
    dado = random.randint(1, 6)
    resultados[dado] += 1
for numero, cantidad in resultados.items():
    print(f"{numero}: {cantidad}")