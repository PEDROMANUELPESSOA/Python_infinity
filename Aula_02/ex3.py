compras = [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]
[fruta1, fruta2, fruta3] = compras
[fruta1_nome, fruta1_valor] = fruta1
[fruta2_nome, fruta2_valor] = fruta2
[fruta3_nome, fruta3_valor] = fruta3
soma = fruta1_valor+fruta2_valor+fruta3_valor
print(soma)

soma=0
for compras in compras:
    soma = compras[1]+soma
print(soma)
