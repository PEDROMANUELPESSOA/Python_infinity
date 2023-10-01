txt = str(input("Digite o nome: "))[::-1]

print(txt)

nome = str(input("Digite o seu nome: "))
nome_lista = list(nome)
nome_lista.reverse()
nome_invertido = "".join(nome_lista)
# nome_invertido = nome[::-1]
print(nome_invertido)