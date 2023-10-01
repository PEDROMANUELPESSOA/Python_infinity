quadrado = lambda valor : valor ** 2

print(quadrado(5))

#------------------------------------------

par = lambda numero : numero % 2 == 0

print(par(8))

#------------------------------------------

maiusculo = lambda palavra : palavra.upper()

print(maiusculo("maria"))

#------------------------------------------

caracteres_palavra = lambda palavra2 : len(palavra2)

print(caracteres_palavra("maria"))

#------------------------------------------

soma = lambda numero1, numero2 : numero1+numero2
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
print(soma(numero1, numero2))

#------------------------------------------

par_ou_impar = lambda numero: f"O número {numero} é par" if numero % 2 == 0 else f"O número {numero} é impar"

numero = int(input("Digite um número: "))
print(par_ou_impar(numero))

#------------------------------------------

