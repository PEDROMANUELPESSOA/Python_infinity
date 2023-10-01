n1 = str(input("Vamos verificar se a letra é M-Masculino ou F-feminino: "))

if n1.isalpha():
    if n1 in "mM":
        print(f"O letra é {n1} - Sexo masculino")
    elif n1 in "fF":
        print(f"O letra é {n1} - Sexo feminino")
    else:
        print(f"O letra é {n1} - Sexo invalido")  
else:
    print(f"O caractere digitado Não é letra.")
