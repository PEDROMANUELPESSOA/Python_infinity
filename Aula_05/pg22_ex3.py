from functools import reduce

lista_de_numeros = [1,170,3,4,5]

maior = reduce(lambda numero_anterior, proximo_numero : numero_anterior if numero_anterior > proximo_numero else proximo_numero, lista_de_numeros)

print(maior)