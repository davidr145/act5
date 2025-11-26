import re
while True:
    password = input("Introduce una contraseña: ")
    if (6 <= len(password) <= 8 and
        len(re.findall(r'[a-z]', password)) >= 2 and
        len(re.findall(r'[A-Z]', password)) >= 1 and
        len(re.findall(r'[1-5]', password)) >= 2 and
        len(re.findall(r'[*_@&/#]', password)) >= 2 and
        len(re.findall(r'[6-9]', password)) >= 1):
        print("Password correcto")
    else:
        print("Password incorrecto")
    respuesta = input("¿Deseas introducir otro password? (s/n): ")
    if respuesta.lower() != 's':
        break