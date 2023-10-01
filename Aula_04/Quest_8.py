
#Questão 8
#Dado o dicionário Filme com a seguinte estrutura {"Titulo" : "It a Coisa", "Genero": "Terror", "Duracao": 120, "Cartaz": False}
#faça um programa que imprima os valores de todas as chaves uma por #uma, e no final remova a chave "Genero" e caso ela não exista, mostre #uma mensagem de erro informando que a chave não existe

filme ={"Titulo" : "It a Coisa", "Genero": "Terror", "Duracao": 120, "Cartaz": False}

lista_chaves = filme.keys()

for chave in lista_chaves:
        print(f"""
            Chave: {chave}
        """)
print(filme)
print(f"""
            Chave Excluída genero: {filme.pop("Genero", "erro a chave não existe")}
        """)
print(filme)