#PRIMEIRA QUESTÃO LOOP
numero = int(input("Digite um número: "))

for i in range(numero, 0, -1):
    print(i)

cont = numero
while cont >= 0:
    print(cont)
    cont -= 1