num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))
if num1 > num2:
    num1, num2 = num2, num1
    pares = [str(x) for x in range(num1, num2+1) if x % 2 == 0]
    impares = [str(x) for x in range(num1, num2+1) if x % 2 != 0]
    print(f"los números pares son {'-'.join(pares)}")
    print(f"los números impares son {'-'.join(impares)}")