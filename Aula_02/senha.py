while True:
    senha = str(input("Digite a senha: "))
    if len(senha) >= 8 and len(senha) <= 12:
        print("Você digitou uma senha válida")
        break
    else:
        print("Senha inválida, digite uma senha com no mínimo 8 caracteres e no máximo 12 ")
