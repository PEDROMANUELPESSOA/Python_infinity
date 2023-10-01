n1 = str(input("Vamos verificar se a letra é Vogal ou Consoante: "))

if n1.isalpha():
    if n1 in "AEIOUaeiou":
        print(f"O letra é {n1} - Vogal")
    else:
        print(f"O letra é {n1} - consoante")  
else:
    print(f"O caractere digitado Não é letra.")
