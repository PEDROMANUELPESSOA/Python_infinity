numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))
numero3 = int(input("Digite um numero: "))
numero4 = int(input("Digite um numero: "))

if numero1 >= numero2 and numero1 >= numero3 and numero1 >= numero4:
    print(numero1)
elif numero2 >= numero1 and numero2 >= numero3 and numero2 >= numero4:
    print(numero2)
elif numero3 >= numero2 and numero3 >= numero1 and numero3 >= numero4:
    print(numero3)
else:
    print(numero4)
