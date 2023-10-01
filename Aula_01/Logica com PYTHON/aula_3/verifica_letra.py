in1 = str(input("Digite a inicial do nome do aluno M ou F: "))

if in1.isalpha():
    if in1=="m" or in1=="M":
        print(f"A inicial é um M.")
    elif in1=="f" or in1=="F":
        print(f"A inicial é um F.")
    else:
            print(f"A inicial do aluno é uma letra do alfabeto diferente de L ou F.")
else:
    print(f"A inicial do aluno Não é letra.")