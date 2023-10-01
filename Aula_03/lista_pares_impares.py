lista_pares = []
lista_impares = []
lista = []

while True:
    novo_numero = int(input("Digite o novo numero: "))
    lista.append(novo_numero)
    if novo_numero%2==0:
        lista_pares.append(novo_numero)
    else:
         lista_impares.append(novo_numero)
    if len(lista) == 10:
        break

for id_lista in lista_pares:
        print(f"Numeros pares da lista: {id_lista}")

for id_lista in lista_impares:
        print(f"Numeros impares da lista: {id_lista}")





lista_dos_pares = []
lista_dos_impares = []

for i in range(10):
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        lista_dos_pares.append(numero)
    else:
        lista_dos_impares.append(numero)

for numero_par in lista_dos_pares:
    print(f"Esse número é par: {numero_par}")

for numero_impar in lista_dos_impares:
        print(f"Esse número é ímpar: {numero_impar}")