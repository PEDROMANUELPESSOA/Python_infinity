soma = 0

for i in range(0,6):
    numero = int(input("Digite um numero: "))
    if numero%2==0:
        soma = soma + numero
print(soma)
