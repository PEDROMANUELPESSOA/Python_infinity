n1 = float(input("Digite o 1° numero: "))
n2 = float(input("Digite o 2° numero: "))

operador = str(input("Digite a operação desejada: "))

if operador=="+":
        print(f"{n1+n2}")
elif operador=="-":
        print(f"{n1-n2}")
elif operador=="*":
        print(f"{n1*n2}")
elif operador=="/":
        print(f"{n1/n2}")
else:
            print(f"A operação digitada não é valida.")

