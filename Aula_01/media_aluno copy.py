alunos = []
nota1 = []
nota2 = []
nota3 = []
nota4 = []
media = []

while True:
    alunos.append(str(input('Digite o nome do aluno: ')))
    nota1.append(int(input('Digite a 1ª nota do aluno: ')))
    nota2.append(int(input('Digite a 2ª nota do aluno: ')))
    nota3.append(int(input('Digite a 3ª nota do aluno: ')))
    nota4.append(int(input('Digite a 4ª nota do aluno: ')))

    continuar = str(input('cadastrar mais? S/N: ')).strip().upper()[0]
    if continuar == 'N':
        break

# D = [(nota1 + nota2 + nota3 + nota4)/4 for nota1, nota2, nota3, nota4 in zip(nota1, nota2, nota3, nota4)]
# print(D)


for nota1, nota2, nota3, nota4 in zip(nota1, nota2, nota3, nota4):
    media.append((nota1 + nota2 + nota3 + nota4)/4)

def formatar(valor):
    return f'{valor:>7}' # alinhar à direita, usando 7 posições

print('Alunos:', *alunos)
print('médias: ', *media)