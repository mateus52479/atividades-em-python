nome = input("digite o nome do produto: ")
quantidade = int(input("digite a quantidade do produto: "))
preco = float(input("digite o preço do produto: "))

bruto = preco * quantidade

tipo_pagamento = int(input("digite a forma de pagamento: \n 1-DINHEIRO \n 2-CARTÃO DE CREDITO \n 3-DUAS VEZES \n 4-TRÊS VEZES \n"))

while True:
    match tipo_pagamento:
        case 1  :
            liquido = bruto - bruto * 0.10
            print(f"o preço final do produto {nome} com {quantidade} itens tem um preço de {liquido}")
            break
        case 2  :
            liquido = bruto - bruto * 0.05
            print(f"o preço final do produto {nome} com {quantidade} itens tem um preço de {liquido}")
            break
        case 3:
            liquido = bruto 
            print(f"o preço final do produto {nome} com {quantidade} itens tem um preço de {liquido}")
            break
        case 4  :
            liquido = bruto + (bruto * 0.10)
            print(f"o preço final do produto {nome} com {quantidade} itens tem um preço de {liquido}")
            break
        case _:
            print("digite uma opção valida(somente numeros de 1 a 4)")
        