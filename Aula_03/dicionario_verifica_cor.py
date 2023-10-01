carro = {
    "Marca": "Ford",
    "Modelo": "Ka",
    "Ano": 2020,
    "Cor": "Cinza"
    }
if ("Cor" in carro):
    del carro["Cor"]
else: 
    carro["Cor"] = "Azul"
    
print(carro)
    
