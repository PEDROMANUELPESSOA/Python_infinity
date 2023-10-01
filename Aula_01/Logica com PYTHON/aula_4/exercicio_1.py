while True:
    sexo = str(input("Digite o sexo (M ou F)"))
    if sexo == "M" or sexo == "F" or sexo == "m" or sexo == "f":
        break
    else:
        print("Valor invalido, digite novamente")