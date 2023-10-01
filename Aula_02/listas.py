#APPEND
lista_alunos = ["Abel", "Aline", "João", "Maria", "Ana", "Pedro"]

novo_aluno = str(input("Digite o nome do novo aluno: "))

lista_alunos.append(novo_aluno)

print(lista_alunos)



#INSERT
lista_alunos = ["Abel", "Aline", "João", "Maria", "Ana", "Pedro"]

novo_aluno = str(input("Digite o nome do novo aluno: "))

lista_alunos.insert(2, novo_aluno)

print(lista_alunos)




#POP MODO NORMAL
lista_alunos = ["Abel", "Aline", "João", "Maria", "Ana", "Pedro"]

item_exluido = lista_alunos.pop()
lista_alunos.pop()

print(lista_alunos)

print(item_excluido)


#POP MODO PSICOPATA
lista_alunos = ["Abel", "Aline", "João", "Maria", "Ana", "Pedro"]


lista_exluidos = [lista_alunos.pop(), lista_alunos.pop()]

print(lista_alunos)

print(lista_exluidos)


#REMOVE
lista_alunos = ["Abel", "Aline", "João", "Maria", "Ana", "Pedro"]

aluno = str(input("Digite o nome do aluno que você deseja remover: "))

lista_alunos.remove(aluno)

print(lista_alunos)



#SORT
lista_alunos = ["Abel",  "João", "Maria", "Ana", "Pedro", "Aline"]

lista_alunos.sort()

print(lista_alunos)



#REVERSE
lista_alunos = ["Abel",  "João", "Maria", "Ana", "Pedro", "Aline"]

lista_alunos.reverse()

print(lista_alunos)




#INDEX
lista_alunos = ["Abel",  "João", "Maria", "Ana", "Pedro", "Aline"]

posicao = lista_alunos.index("Maria")

print(lista_alunos)




#COUNT
lista_alunos = ["Abel",  "João", "Maria", "Ana", "Pedro", "Aline" ,"Maria"]

quantidade = lista_alunos.count("Maria")

print(quantidade)



#DESCOMPACTANDO UMA TUPLA
linguagens = ("Javascript", "Python", "Java", "PHP")

(js, py, java, php) = linguagens

ling1 = linguagens[0]
ling2 = linguagens[1]
ling3 = linguagens[2]
ling4 = linguagens[3]

print(ling2)
print(py)



#ITERAÇÃO
linguagens = ("Javascript", "Python", "Java", "PHP")

# print(linguagens[0])
# print(linguagens[1])
# print(linguagens[2])
# print(linguagens[3])

# for i in range(4):
#     print(linguagens[i])

for linguagem in linguagens:
    print(linguagem)


