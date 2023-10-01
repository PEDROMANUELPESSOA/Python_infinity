from tkinter import *

# -------------------------------------
janela = Tk()
resposta = StringVar()

def enigmatica():
    if int(numero1.get()) >= int(numero2.get()):
        return resposta.set(f"O maior numero é: {numero1.get()}")
    else:
        return resposta.set(f"O maior numero é: {numero2.get()}")

azul_claro = "#558b9e"

titulo = Label(text="Bem vindo",bg="red", fg="white", width="60")
titulo.pack()

nome_texto = Label(text="Maior numero?")
nome_texto.pack()

#https://mybrandnewlogo.com/pt/gerador-de-paleta-de-cores extensions=Color Highlight

nome_texto3 = Label(text="Digite o primeiro número: ")
nome_texto3.pack()
numero1 = Entry(bg="#003e2a", fg=azul_claro, width="40")
numero1.pack()

nome_texto4 = Label(text="Digite o segundo número: ")
nome_texto4.pack()
numero2 = Entry(bg="#003e2a", fg=azul_claro, width="40")
numero2.pack()

resultado = Label(textvariable=resposta,bg="#003e2a", fg=azul_claro, width="30")
resultado.pack()

botao_enviar = Button(janela, text="Enviar", width=20, bg=azul_claro, command=enigmatica)
botao_enviar.pack()




janela.mainloop()

# -------------------------------------
