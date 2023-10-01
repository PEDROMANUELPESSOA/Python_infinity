from tkinter import *

janela = Tk()

def saudacao():
    print(f"Seja bem vindo {nome_entrada.get()}")
    nome_entrada.delete(0, END)

azul_claro = "#558b9e"

titulo = Label(text="Bem vindo",bg="red", fg="white")
titulo.pack()

nome_texto = Label(text="Nome")
nome_texto.pack()

#https://mybrandnewlogo.com/pt/gerador-de-paleta-de-cores extensions=Color Highlight

nome_entrada = Entry(bg="#003e2a", fg=azul_claro, width="60")
nome_entrada.pack()


botao_enviar = Button(janela, text="Enviar", width=30, bg=azul_claro, command=saudacao)
botao_enviar.pack()

janela.mainloop()