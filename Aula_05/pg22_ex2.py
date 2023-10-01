lista = ["joao", "mariaa", "joseee"]

quant1 = lambda palavra : len(palavra)>5

quant2 = list(filter(quant1, lista ))

print(quant2)