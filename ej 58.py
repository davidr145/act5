import random
numeroaleatorio= random.randint (1, 5)
intentos=3
while intentos>0:
    intento= int(input("introduce el valor que crees que es:"))
    if intento == numeroaleatorio:
        print("has acertado el numero")
    else:
        print("has fallado, no es el numero introducido.")
        intentos-=1