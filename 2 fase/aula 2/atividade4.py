dicionario = {"Poma": 6.9, "guinas" : 2.0, "japa" : 8.0}

for nome, nota in dicionario.items():
    if nota >= 7:
        print(f"O {nome} está na média")