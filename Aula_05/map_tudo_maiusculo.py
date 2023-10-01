

lista = ["joao", "maria", "jose"]

maiusculo = lambda palavra : palavra.upper()

maiusculo2 = list(map(maiusculo, lista ))

print(maiusculo2)