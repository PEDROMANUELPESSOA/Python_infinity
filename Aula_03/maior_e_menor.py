lista = []

while True:
    novo_numero = int(input("Digite o novo numero: "))
    lista.append(novo_numero)
    if len(lista) == 10:
        break
    
maximo = lista[0]
for i in range(0,len(lista)):
    if lista[i]>maximo:
        maximo = lista[i]
print(maximo)

minimo = lista[0]
for i in range(0,len(lista)):
    if lista[i]<minimo:
        minimo = lista[i]
print(minimo)





maior_valor = 0
menor_valor = float("inf")

for i in range(10):
    numero = int(input("Digite um número: "))

    if numero >= maior_valor:
        maior_valor = numero
    
    if numero <= menor_valor:
        menor_valor = numero

print(maior_valor)
print(menor_valor)
    
