while True:
    combustivel = input("digite os combustiveis disponiveis (alcool ou gasolina): ").lower()
    quantidade = float(input("digite a quantidade de combustivel a adicionar: "))
    

    if combustivel == "alcool":
        liquido = 4.22 * quantidade
        print(f"preço bruto: {liquido}")
        if quantidade <= 20:
            liquido -= (liquido * 0.03)
            break
        else:
            liquido -= (liquido * 0.05)
            break

    elif combustivel == "gasolina":
        liquido = 5.65 * quantidade
        print(f"preço bruto: {liquido}")
        
        if quantidade <= 20:
            liquido -= (liquido * 0.04)
            break
        else:
            liquido -= (liquido * 0.06)
            break

    else:
        print("digite um combustivel possivel")

print(f"preço liquido: {liquido}")