lista = []

while True:
    novo_numero = int(input("Digite o novo numero: "))
    lista.append(novo_numero)
    if len(lista) == 10:
        break

for id_lista in lista:
    if id_lista%2 == 0:
        print(id_lista)