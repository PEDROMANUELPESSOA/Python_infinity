#Questão 6
#Dado o array ["Banda", "Musica"], crie apartir desse array um dicionário  e depois insira na key Banda o valor "Iron Maiden", e no campo "Música" o valor "Powerslave",depois faça uma busca nesse objeto criado cuja busca irá buscar por duas chaves diferentes, uma chave chamada Banda  e outra chave chamada "Integrantes", caso a chave exista dentro do dicionário mostre ela na tela, caso não existe mostra uma mensagem informando que a chave procurada não existe
#https://dontpad.com/717/aula-4/python

lista = ["Banda", "Musica"]
dicionario = dict.fromkeys(lista)

dicionario["Banda"] = "Iron Maiden"
dicionario["Musica"] = "Powerslave"

print(dicionario.get("Banda", "A chave procurada não existe"))
print(dicionario.get("Integrantes", "A chave procurada não existe"))

print(dicionario)

