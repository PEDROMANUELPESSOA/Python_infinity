
#.items()

dicionario = {
    "Modulo": "Python",
    "Instituicao": "Infinity School"
}
lista = dicionario.items()


for chave, valor in lista:
        print(f"""
             Chave: {chave}
             Valor: {valor}
         """)

for item in lista:
    print(f"""
            Chave: {item[0]}
            Valor: {item[1]}
        """)

#Questão 6
Dado o array ["Banda", "Musica"], crie apartir desse array um dicionário  e depois insira na key Banda o valor "Iron Maiden", e no campo "Música" o valor "Powerslave",depois faça uma busca nesse objeto criado cuja busca irá buscar por duas chaves diferentes, uma chave chamada Banda  e outra chave chamada "Integrantes", caso a chave exista dentro do dicionário mostre ela na tela, caso não existe mostra uma mensagem informando que a chave procurada não existe


lista = ["Banda", "Musica"]
dicionario = dict.fromkeys(lista)

dicionario["Banda"] = "Iron Maiden"
dicionario["Musica"] = "Powerslave"

print(dicionario.get("Banda", "A chave procurada não existe"))
print(dicionario.get("Integrantes", "A chave procurada não existe"))

print(dicionario)



.items()

dicionario = {
    "Modulo": "Python",
    "Instituicao": "Infinity School"
}
lista = dicionario.items()


for chave, valor in lista:
        print(f"""
             Chave: {chave}
             Valor: {valor}
         """)

for item in lista:
    print(f"""
            Chave: {item[0]}
            Valor: {item[1]}
        """)


#Questão 7
#Dado o dicionário Turma com a seguinte estrutura {"Modulo": "Python", "Duracao": 4.5, "Nome": "717 DFS", "Alunos": 15}
#faça um programa que itere sobre essa dicionario como uma lista e mostre na tela o nome da chave - o valor e depois mostre usando a função keys apenas as chaves que existem nesse dicionário


    print(chave)turma = {"Modulo": "Python", "Duracao": 4.5, "Nome": "717 DFS", "Alunos": 15}

lista_tuplas = turma.items()
for chave, valor in lista_tuplas:
    print(f"{chave} - {valor}")

lista_chaves = turma.keys()
for chave in lista_chaves:


#Questão 8
#Dado o dicionário Filme com a seguinte estrutura {"Titulo" : "It a Coisa", "Genero": "Terror", "Duracao": 120, "Cartaz": False}
#faça um programa que imprima os valores de todas as chaves uma por #uma, e no final remova a chave "Genero" e caso ela não exista, mostre #uma mensagem de erro informando que a chave não existe


filme = {
    "Titulo" : "It a Coisa",
    "Genero": "Terror",
    "Duracao": 120,
    "Cartaz": False
    }

lista_de_valores = filme.values()

for valor in lista_de_valores:
    print(valor)

filme.pop("Genero", "A chave não existe")

print(filme)


#QUESTÃO 9
#Dado o dicionário Jogo com a seguinte estrutura {"Título" : "League of Legends", "Gênero" : "MOBA" }
#faça um programa que faça uma copia desse dicionário, e depois atualize a cópia com um novo título (Perfect World)
# e um novo gênero (MMORPG) e crie também uma novo chave e valor chamado "Lançamento" : 2005

jogo = {"Título" : "League of Legends",
         "Gênero" : "MOBA" 
        }

jogo_copia = jogo.copy()

alteracoes = {
    "Título" : "Perfect World",
    "Gênero" : "MMORPG",
    "Lançamento": 2005 
    }


jogo_copia.update(alteracoes)
# jogo_copia.update({
#     "Título" : "Perfect World",
#     "Gênero" : "MMORPG",
#     "Lançamento": 2005 
#     })




#QUESTÃO 1
#Dado o conjunto Ocupações com a seguinte estrutura {"Jogos", "Luta", "Trabalho", "Namoro"}
#faça um programa que verifique se o elemento "Cozinhar" existe no conjunto, e exiba uma
# mensagem dependendo se existe ou não, depois mostre na tela o tamanho desse conjunto


RESPOSTA DE QUEM VAI NO PSIQUIATRA COM FREQUÊNCIA

ocupacoes = {"Jogos", "Luta", "Trabalho", "Namoro"}

if ("Cozinhar" in ocupacoes):
    print("Cozinhar é uma ocupação")
else:
    print("Cozinhar não é uma ocupação")

print(f"Você tem {len(ocupacoes)} ocupações")

----------------------------------------------------

Resposta do demonio:

conjunto = {"Jogos", "Luta", "Trabalho", "Namoro"}

elemento = [elem for elem in conjunto if elem == "Cozinhar"]
print(f"Elemento não existe")

print(f"Você tem {len(conjunto)} ocupações")




#QUESTÃO 2
#Dado o conjunto Linguagens com a seguinte estrutura {"Python", "Javascript", "Java", "PHP", "C++", "C#"}
#faça um programa que cheque a linguagem "TypeScript" existe nesse conjunto, e mostre na tela de acordo
# depois faça uma cópia desse conjunto, e mostre na tela os dois conjuntos, o original e a copia


linguagens = {"Python", "Javascript", "Java", "PHP", "C++", "C#"}

if ("TypeScript" not in linguagens):
    print("Você não sabe TypeScript")
else:
    print("Você sabe TypeScript")

copia = linguagens.copy()

print(linguagens)
print(copia)

----------------------------------------------------

Versão alternativa de quem trabalha com c sharp:

languages = {"Python", "Javascript", "Java", "PHP", "C++", "C#"}

language = [language for language in languages if language != "Typescript"]
print(f"O cara não sabe Typescript")

copy_languages = languages
print(copy_languages)
print(languages)

#QUESTÃO 3
#Dado o conjunto Cores com a seguinte estrutura {"Amarelo", "Azul", "Vermelho", "Verde"}
#faça um programa que peça uma cor ao usuário e guarde essa cor em uma lista, o programa
#pedirá cores ao usuário até ele digitar a palavra chave "sair", quando o usuário sair do
#programa faça ele inserir todas as cores da lista dentro do conjunto e depois mostrar o conjunto na tela


cores = {"Amarelo", "Azul", "Vermelho", "Verde"}
lista_cores = []

while True:
    cor = str(input("Digite uma cor: "))
    if cor == "sair":
        break
    lista_cores.append(cor)

cores.update(lista_cores)

print(cores)


#QUESTÃO 4
#Dado o conjunto Objetos com a seguinte estrutura {"Relógio", "Garrafa", "Mouse", "Monitor"}
#faça um programa que remova o objeto "Garrafa" do conjunto depois mostre como o conjunto ficou
#na tela, depois limpe o conjunto, e mostre o conjunto vazio na tela



