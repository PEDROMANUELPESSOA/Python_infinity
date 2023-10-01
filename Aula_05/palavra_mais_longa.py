def palavra_mais_longa(lista):

    palavra_maior = lista[0]

    for palavra_atual in lista:
        if len(palavra_atual) >= len(palavra_maior):
            palavra_maior = palavra_atual

    return palavra_maior


alunos = ["Julio", "Abelardo", "João", "Maria", "Ana", "Aline", "Washington"]

print(palavra_mais_longa(alunos))