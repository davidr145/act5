total= 0
repeticiones= 0
while total < 50 or total % 2 == 0:
    num1=input("introduce un primer valor")
    num2=input("introduce un segundo valor")
    suma = int(num1) + int(num2)
    total += suma
    repeticiones += 1
    print (f"la suma es {suma}")
    if repeticiones == 1:
        print(f"el resultado acumulado es {total} y llevas {repeticiones} repeticion")
    else:
        print(f"el resultado acumulado es {total} y llevas {repeticiones} repeticiones")   
print("programa finalizado")