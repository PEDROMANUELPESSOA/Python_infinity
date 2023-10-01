maior_que_10 = lambda numero : numero if numero>10 else numero/2

numero = int(input("Digite o numero: "))


print(maior_que_10(numero))