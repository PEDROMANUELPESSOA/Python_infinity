Animal =  {
    "Especie": "Cachorro", 
    "Raça": "Pinscher", 
    "Idade": 3, 
    "Adestrado": "Sim"
    }

if Animal["Idade"]>2:
    Animal['Vacinado']=True
else:
    Animal['Adestrado']="Não"

print(Animal)