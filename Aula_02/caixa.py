soma = 0

while True:
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: "))
    if preco == -1:
        break


    soma = soma +  preco


