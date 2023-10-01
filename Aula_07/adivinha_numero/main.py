from funcoes import *
import random

aleatorio = gerar()

while True:
    print(aleatorio)

    opcao = int(input("Digite uma tentativa de acertar o numero aleatório entre 0 e 10:"))

    if opcao > aleatorio:
        maior()
    if opcao < aleatorio:
        menor()
    if opcao == aleatorio:
        igual()
        break

    print("\n" * 1)