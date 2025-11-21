total= 0
repeticiones= 0
while total < 50:
    num1=input("introduce un primer valor")
    num2=input("introduce un segundo valor")
    suma = int(num1) + int(num2)
    total += suma
    repeticiones += 1
    print(f"el resultado acumulado es {total} y llevas {repeticiones} repeticion/repeticiones.")
print("programa finalizado")