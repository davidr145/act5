repetir ="s"
while repetir.lower() == "s":
    num1=input("introduce un primer valor")
    num2=input("introduce un segundo valor")
    suma = int(num1) + int(num2)
    print(f"el resultado es:{suma}")
    repetir = input("deseas repetir otra suma? s/n")
print("programa finalizado")
