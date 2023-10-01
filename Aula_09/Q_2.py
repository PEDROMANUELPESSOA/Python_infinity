
#FAÇA UM PROGRAMA QUE RECEBE O NOME DE UM ALUNO
#RECEBE 4 NOTAS DESSE ALUNO
#E MOSTRA NA TELA QUAL FOI A MÉDIA DAS NOTAS
#E TAMBÉM MOSTRE UM TEXTO DA COR VERDE ESCRITO "APROVADO"
#SE A MÉDIA FOR MAIOR OU IGUAL A 6 E UM TEXTO VERMELHO ESCRITO
#"REPROVADO" SE A NOTA FOR ABAIXO DE 6


from tkinter import *

def checagem():
    numero1 = int(numero1_entry.get())
    numero2 = int(numero2_entry.get())
    numero3 = int(numero3_entry.get())
    numero4 = int(numero4_entry.get())
    nome = titulo_entry.get()

    media = (numero1+numero3+numero2+numero4)/4
    resultado.config(text=f"Para o Aluno {nome} a media foi {media}")
    if media >= 6:
        resposta.config(fg="green", text=f"Aprovado")
    else:
        resposta.config(fg="red", text=f"Reprovado")

janela = Tk()

titulo = Label(text="Digite o nome do aluno")
titulo.pack()

titulo_entry = Entry()
titulo_entry.pack()

numero1_label = Label(text="Digite a 1° nota: ").pack()
numero1_entry = Entry()
numero1_entry.pack()

numero2_label = Label(text="Digite a 2° nota: ").pack()
numero2_entry = Entry()
numero2_entry.pack()

numero3_label = Label(text="Digite a 3° nota: ").pack()
numero3_entry = Entry()
numero3_entry.pack()

numero4_label = Label(text="Digite a 4° nota: ").pack()
numero4_entry = Entry()
numero4_entry.pack()


resultado = Label(text="")
resultado.pack()

resposta = Label(text="")
resposta.pack()

botao_checar = Button(janela, text="Checando", command=checagem).pack()


janela.mainloop()