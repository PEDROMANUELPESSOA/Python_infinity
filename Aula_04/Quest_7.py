
#Questão 7
#Dado o dicionário Turma com a seguinte estrutura {"Modulo": "Python", "Duracao", 4.5, "Nome": "717 DFS", "Alunos": 15}
#faça um programa que itere sobre essa dicionario como uma lista e mostre na tela o nome da chave - o valor e depois mostre usando a função keys apenas as chaves que existem nesse dicionário

Turma = {"Modulo": "Python", "Duracao": 4.5, "Nome": "717 DFS", "Alunos": 15}

lista = Turma.items()

for item in lista:
    print(f"""
            Chave: {item[0]}
            Valor: {item[1]}
        """)
    
lista_chaves = Turma.keys()
for chave in lista_chaves:
        print(f"""
            Chave: {chave}
        """)