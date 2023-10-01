numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operação = str(input("Digite uma operação [ + | - | * | / ]: "))
resultado = 0

if operação == "+":
    resultado = numero1 + numero2
elif operação == "-":
    resultado = numero1 - numero2
elif operação == "*":
    resultado = numero1 * numero2
elif operação == "/":
    resultado = numero1 / numero2
else:
    print("Operação inválida")


if resultado % 2 == 0:
    print(f"O resultado é {resultado} e é par ")
else:
    print(f"O resultado é {resultado} e é ímpar ")

if resultado > 0:
    print(f"O resultado é {resultado} e é positivo ")
elif resultado < 0:
    print(f"O resultado é {resultado} e é negativo ")
else:
    print(f"O resultado é {resultado} e é neutro ")

if resultado == int(resultado):
    print(f"O resultado é {resultado} e é inteiro ")
else:
    print(f"O resultado é {resultado} e é decimal ")


