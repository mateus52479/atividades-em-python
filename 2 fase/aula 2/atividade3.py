lista = [("ana", 17), ("Carlos", 20), ("joão", 15)]
conta = 0
index = 0

mais_velho = lista[0]

for pessoa in lista:
    if pessoa[1] > mais_velho[1]:
        mais_velho = pessoa

print(f"A pessoa mais velha é {mais_velho[0]} com {mais_velho[1]} anos.")