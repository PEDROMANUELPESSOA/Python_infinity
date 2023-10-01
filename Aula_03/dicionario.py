estrutura = {"Nome": "Abel", "Idade": "28", "Altura": 1.79, "Habilitacao": True}
estrutura['Nota']=9
del estrutura["Altura"]



print(list(estrutura))
print(len(estrutura))
print(estrutura['Idade'])
print(estrutura['Nota'])
print("Altura" in estrutura)
print("Nota" in estrutura)

estrutura2=estrutura.copy()


print("Nome" not in estrutura)
print("Chuva" not in estrutura)
print(iter(estrutura))
print(estrutura.keys())

estrutura.clear()


print(estrutura2)
print(estrutura)

# 01
# chave not in dicionario
# Retorna True se a chave não for encontrada no dicionário,
# senão, retornará False

# 02 
# iter()
# Retorna um iterador para as chaves do dicionário. Retorna o
# mesmo que dicionario.keys()

# 03
# dicionario.clear()
# Remove todos os itens do dicionário

# 04
# dicionario.copy()
# Retorna uma cópia do dicionário

# 05 
# dict.fromkeys(iteravel)
# Cria um novo dicionário com chaves proveniente do iteravel
# (uma lista, um dicionário), os valores por padrão serão None

# 06 
# dicionario.get(chave, valor padrão)
# retorna o valor para a chave especificada se esta existir no
# dicionário, senão, será retornado um valor padrão definido. Caso
# este valor não seja definido, a função retornará None