par = 0
impar = 0
inicial = int(input("Digite o inicial final para contar os pares e impares: "))
final = int(input("Digite o numero final para contar os pares e impares: "))

for i in range(inicial,final+1):
        if i%2==0:
         par = par + 1
         print(f"este é um par: {i}")
        else:
            impar = impar +1

        
print(f"A quantidade de numero par é {par}")
print(f"A quantidade de numero impar é {impar}")


