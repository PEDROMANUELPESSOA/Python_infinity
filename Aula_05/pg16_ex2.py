maior_que_5 = lambda palavra1, palavra2 : f"{palavra1} {palavra2}" if len(palavra1) > 5 and len(palavra2) > 5 else "erro"

palavra1 = str(input("Digite a primeira palavra: "))
palavra2 = str(input("Digite a segunda palavra: "))

print(maior_que_5(palavra1, palavra2))