import random
lista = []
while True:
    lista.append(str(input('Digite o nome do cliente para confirmar sua inscrição no sorteio: ')))
    continuar = str(input('Fechar o caixa? S/N: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('O sorteado é {}'.format(random.choice(lista)))