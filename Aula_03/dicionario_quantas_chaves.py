estrutura = {"Nome": "Abel", "Idade": "28", "Altura": 1.79, "Habilitacao": True}
estrutura['Nota']=9
del estrutura["Altura"]



print(list(estrutura))
print(len(estrutura))
print(estrutura['Idade'])
print(estrutura['Nota'])
print("Altura" in estrutura)
print("Nota" in estrutura)
print(estrutura)