#QUESTÃO 9
#Dado o dicionário Jogo com a seguinte estrutura {"Título" : "League of Legends", "Gênero" : "MOBA" }
#faça um programa que faça uma copia desse dicionário, e depois atualize a cópia com um novo título (Perfect World)
# e um novo gênero (MMORPG) e crie também uma novo chave e valor chamado "Lançamento" : 2005


jogo =  {"Título" : "League of Legends", "Gênero" : "MOBA" }

jogo2 = jogo.copy()

alteraçoes = {
    "Título" : "Perfect World", 
    "Gênero" : "MMORPG",
    "Lançamento" : 2005
}

print(jogo2)

jogo2.update(alteraçoes)

print(jogo2)