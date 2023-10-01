# print("Hello Word")

# nome = str(input("Digite o seu nome: "))
# sobrenome = str(input("Digite o seu sobrenome: "))

# print("Meu nome é", nome, "e Meu sobrenome é", sobrenome)

# print(f"Meu nome é {nome} e Meu sobrenome é {sobrenome}")

# n1 = int(input("Digite o 1° numero: "))
# n2 = int(input("Digite o 2° numero: "))

# n3=n1+n2

# print(f"O 1° numero é {n1}, O 2° numero é {n2} A soma é {n3}")

in1 = str(input("Digite a inicial do nome do aluno: "))
n1 = float(input("Digite a 1° nota: "))
n2 = float(input("Digite a 2° nota: "))
n3 = float(input("Digite a 3° nota: "))
n4 = float(input("Digite a 4° nota: "))

n5=(n1+n2+n3+n4)/4

print(f"A 1° nota é {n1}, A 2° nota é {n2}, A 3° nota é {n3},A 4° nota é {n4},A média é {n5},")

if n5 == 5:
    print("Aluno Aprovado")

else:
    print("Aluno Reprovado")

    maior = n1
if n2>n1 and n2>n3 and n2>n4 or n1==n2 or n3==n2 or n4==n2:

    maior = n2
if n3>n1 and n3>n2 and n3>n4 or n1==n3 or n2==n3 or n4==n3:

    maior = n3
if n4>n1 and n4>n2 and n4>n3 or n1==n4 or n2==n4 or n3==n4:

    maior = n4

menor = n1
if n2<n1 and n2<n3 and n2<n4 or n1==n2 or n3==n2 or n4==n2:


    menor = n2
if n2<n1 and n2<n3 and n2<n4 or n1==n2 or n3==n2 or n4==n2:


    menor = n3
if n2<n1 and n2<n3 and n2<n4 or n1==n2 or n3==n2 or n4==n2:

    menor = n4

print(f"A menor nota foi {menor}")
print(f"A maior nota foi {maior}")

if in1.isalpha():
    if in1=="a" or in1=="e" or in1=="i" or in1=="o" or in1=="u" or in1=="A" or in1=="E" or in1=="I" or in1=="O" or in1=="U":
        print(f"A inicial é uma vogal.")
    else:
        print(f"A inicial é uma consoante.")
else:
    print(f"A inicial do auluno Não é letra.")

if in1.isalpha():
    if in1 in 'aeiouAEIOU':
        print(f"A inicial é uma vogal.")
    else:
        print(f"A inicial é uma consoante.")
else:
    print(f"A inicial do auluno Não é letra.")    

          
maior2 = max(n1, n2, n3, n4)
print(f"A maior nota é {maior2}.")    

