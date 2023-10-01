from funcoes import *



while True:
    escolha = input("Digite uma das opções abaixo\n"
                    "1 - Cadastrar novo\n"
                    "2 - Ver Lista\n"
                    "0 - Finalizar sistema\n")
    
    match escolha:
        case "1":
            nome = input("Digite o Nome: ")
            telefone = int(input("Digite telefone: "))
            cadastroAluno(nome, telefone)
        case "2":
            print(dados)

            print("\n" * 1)