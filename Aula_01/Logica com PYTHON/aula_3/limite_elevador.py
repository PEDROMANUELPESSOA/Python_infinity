n1 = str(input("Digite quantidade de pessoas no elevador: "))


if n1.isnumeric():
    if n1 <= 8:
        print("O elevador será ativado")
    else:
        print(f"O elevador não sequirá com {n1} pessoas. O limite é 8 pessoas")
else:
    print("Não digitou numero.")