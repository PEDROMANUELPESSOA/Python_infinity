from operacoes import *

while True:
    opcao = input(
                    "1 - Somar\n"
                    "2 - Subtrair\n"
                    "3 - Multiplicação\n"
                    "4 - Divisão\n"
                    "0 - Finalizar sistema\n"
                    "Digite uma das opções:")
    
    match opcao:
        case "1":
            soma()
        case "2":
            subtracao()
        case "3":
            multiplicacao()
        case "4":
            divisao()
        case "0":
            break

    print("\n" * 1)