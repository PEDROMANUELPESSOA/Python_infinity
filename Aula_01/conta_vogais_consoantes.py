#TERCEIRA QUESTÃO
#QUINTA QUESTÃO
frase = str(input("Digite uma frase: "))
contador = 0
contador_consoante = 0
for letra in frase:
    if letra in "aeiouAEIOU":
        contador += 1
    else:
        contador_consoante += 1
print(f"O número de vogais da frase é : {contador}")
print(f"O número de consoantes da frase é : {contador_consoante}")