
soma_idade = 0
mais_velha = 0
nome_mais_velha = ""
menos_de_20 = 0
sexo_mais_velha = ""

for i in range(0,3):
    nome = str(input("Digite o nome do aluno: "))
    idade = int(input("Digite a idade do aluno: "))
    sexo = str(input("Digite a inicial do sexo do aluno M ou F: "))
    
    if sexo.isalpha():
        if sexo=="m" or sexo=="M":
         sexo="Masculino"
        elif sexo=="f" or sexo=="F":
         sexo="Feminino"
        else:
            sexo = str(input("Digite a inicial do sexo do aluno M ou F: "))
    else:
     sexo = str(input("Digite a inicial do sexo do aluno M ou F: "))

    soma_idade = soma_idade + idade



    if idade >= mais_velha:
        mais_velha = idade
        nome_mais_velha = nome
        sexo_mais_velha = sexo

    if idade <= 20:
        menos_de_20 = menos_de_20+1

media = soma_idade / 3

print(f"A media das idades é: {media}")
print(f"A pessoa mais velha é {nome_mais_velha}, a idade é {mais_velha}, e o sexo é {sexo_mais_velha}.")
print(f"Ocorreram {menos_de_20} pessoas com menos de 20 anos")