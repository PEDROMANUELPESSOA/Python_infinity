import random

pontos_do_usuario = 0
pontos_do_computador = 0
contador_de_empates = 0

def escolher_usuario():
    escolha_do_usuario = str(input("Escolha entre Pedra, Papel ou Tesoura: ")).lower()
    return escolha_do_usuario

def escolher_computador():
    lista = ['pedra', 'papel', 'tesoura']
    escolha_do_computador = random.choice(lista)
    return escolha_do_computador

def checar_vencedor(escolha_do_usuario, escolha_do_computador):
    global pontos_do_usuario
    global pontos_do_computador
    global contador_de_empates

    if escolha_do_usuario == escolha_do_computador:
        contador_de_empates += 1
        return "deu empate"
    elif escolha_do_usuario == 'papel' and escolha_do_computador == 'pedra':
        pontos_do_usuario += 1
        return "O usuário ganhou"
    elif escolha_do_usuario == "pedra" and escolha_do_computador == "tesoura":
        pontos_do_usuario += 1
        return "O usuário ganhou"
    elif escolha_do_usuario == 'tesoura' and escolha_do_computador == 'papel':
        pontos_do_usuario += 1
        return "O usuário ganhou"
    else:
        pontos_do_computador +=1
        return "O computador ganhou"


def jogar():
        escolha_do_usuario = escolher_usuario()
        escolha_do_computador = escolher_computador()

        print(f"""
            Escolha do usuário: {escolha_do_usuario}
            Escolha do computador: {escolha_do_computador}
        """)

        resultado_final = checar_vencedor(escolha_do_usuario, escolha_do_computador)

        print(resultado_final)

def ver_placar():
    return f"""
                             
        Usuário  {pontos_do_usuario} vs {pontos_do_computador} Computador
    """

def checar_campeao():
    global pontos_do_usuario
    global pontos_do_computador
    global contador_de_empates

    print(f"Total de empates: {contador_de_empates}")

    if pontos_do_computador > pontos_do_usuario:
        return f"O computador venceu de {pontos_do_computador} x {pontos_do_usuario} do usuário"
    elif pontos_do_usuario > pontos_do_computador:
        return f"O usuário venceu de {pontos_do_usuario} x {pontos_do_computador} do computador"
    else:
        return f"Jogo empatado"

def mostar_menu():
    menu = int(input("""
        O que você quer fazer:
        1 - Jogar
        2 - Ver o placar
        3 - Sair
    """))
    return menu

while True:
    
    menu = mostar_menu()
    if menu == 1:
       jogar()
    elif menu == 2:
        print(ver_placar())
    elif menu == 3:
        print(checar_campeao())
        break
    else:
        print("Opção inválida, escolha novamente")



   

