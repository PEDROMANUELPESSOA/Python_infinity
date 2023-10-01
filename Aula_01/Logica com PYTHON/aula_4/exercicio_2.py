num1 = float(input("Digite o primeiro valor:"))
num2 = float(input("Digite o segundo valor:"))


while True:
    menu = int(input("""
                    Digite:
                    1 para somar
                    2 para multiplicar
                    3 para Dividir
                    4 para subtrair
                    5 para sair
    """))

    if menu == 1:
        print(f"A soma dos numeros é : {num1 + num2}")
    elif menu == 2:
        print(f"A multiplicação dos numeros é : {num1 * num2}")
    elif menu == 3:
        print(f"A divisao dos numeros é : {num1 / num2}")
    elif menu == 4:
        print(f"A subtração dos numeros é : {num1 - num2}")
    elif menu == 5:
        print(f"volte sempre :D")
        break           
    else:
        print("Opção invalida, digite novamente")