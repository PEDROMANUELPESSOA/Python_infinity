numero = " "

inicial = int(input("Digite o inicial final para contar: "))
final = int(input("Digite o numero final para contar: "))

for i in range(inicial,final+1):
          print(i)
          numero = numero + " " + str(i)

print(numero)

