from functools import reduce

lista_de_numeros = [1,2,3,4,5]

soma = reduce(lambda numero_anterior, proximo_numero : numero_anterior + proximo_numero, lista_de_numeros)

print(soma)