import random

while True:

    lista = ["pedra", "papel", "tesoura"]


    escolha_usuario = print(str(input("escolha entre Pedra, Papel ou Tesoura")))
    escolha_maquina = random.choice(lista)

    def jogo(escolha_usuario, escolha_maquina):
        if escolha_usuario == escolha_maquina:
            return print("EMPATE")
        elif escolha_usuario == "pedra" and escolha_maquina == "tesoura":
            return print("VOCÊ VENCEU")
        elif escolha_usuario == "papel" and escolha_maquina == "pedra":
            return print("VOCÊ VENCEU")
        elif escolha_usuario == "tesoura" and escolha_maquina == "papel":
            return print("VOCÊ VENCEU")
        else:
            return print("A MAQUINA VENCEU")
