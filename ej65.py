numeros = []
while True:
    num = int(input("Introduce un número (-99 para terminar): "))
    if num == -99:
        break
    numeros.append(num)
if numeros:
    print(f"El número mayor es: {max(numeros)}")
    print(f"El número menor es: {min(numeros)}")
else:
    print("No se introdujeron números")