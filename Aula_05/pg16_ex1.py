par_ou_impar = lambda numero: f"O número {numero} é par" if numero % 2 == 0 else f"O número {numero} é impar"

numero = int(input("Digite um número: "))
print(par_ou_impar(numero))