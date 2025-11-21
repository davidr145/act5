repetir ="s"
total= 0
repeticiones= 0
while repetir.lower() == "s":
    num1=input("introduce un primer valor")
    num2=input("introduce un segundo valor")
    suma = int(num1) + int(num2)
    print(f"el resultado es:{suma}")
    total += suma
    repetir = input("deseas repetir otra suma? s/n")
    repeticiones += 1
print(f"la suma total de todos los valores es {total} y el numero de repeticiones es {repeticiones}")   
print("programa finalizado")