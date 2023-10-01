import random

lista = []

while True:
    nome = str(input("Digite o nome: "))
    if nome == "fim":
        break
    telefone = int(input("Digite o numero com DDD: (sem caracteres especial)"))

    lista.append([nome, telefone])

cliente_sorteado = random.choice(lista)

print(f'O sorteado foi:{cliente_sorteado[0]} {cliente_sorteado[1]}')

    
