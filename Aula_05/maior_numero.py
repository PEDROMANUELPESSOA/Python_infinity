def enigmatica(numero1, numero2):
    if numero1 >= numero2:
        return numero1
    else:
        return numero2
    

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print(enigmatica(numero1, numero2))