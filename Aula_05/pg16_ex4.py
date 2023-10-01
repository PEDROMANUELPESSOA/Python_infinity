divisivel_por_3_por_5 = lambda numero : "divisivel" if numero % 3 == 0 and numero % 5 == 0 else "nao é divisivel"

numero = int(input("Digite o número: "))

print(divisivel_por_3_por_5(numero))