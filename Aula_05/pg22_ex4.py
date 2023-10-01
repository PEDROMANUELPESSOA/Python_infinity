lista = [
    {
    "nome":"pedro", 
    "idade":13
    },
    {
    "nome":"joao", 
    "idade":15
    },
    {
    "nome":"maria", 
    "idade":19
    }
    ]

nome1 = lambda palavra : palavra["nome"]

nome2 = list(map(nome1, lista ))

print(nome2)