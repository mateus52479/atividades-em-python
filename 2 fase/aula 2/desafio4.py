estoque = {}
while True: 
    pergunta = input("digite um comando:\n\n1) Adicionar produto\n\n2) Atualizar quantidade\n\n3) Calcular valor total do estoque\n\n4) Listar todos os produtos com preço e quantidade\n\nresposta: ")

    match pergunta:
        case "1":
            produto = input("digite o nome do produto: ")
            preco = float(input("digite o preço do produto: "))
            quantidade = int(input("digite a quantidade do produto: "))

            estoque[produto] =  {"preço": preco, "quantidade": quantidade}
            print(estoque)

        case "2":
            produto = input("digite o nome do produto à atualizar a quantidade: ")
            quantidade = int(input("digite a nova quantidade do produto: "))

            for i in estoque:
                if produto in estoque:
                    estoque[produto]["quantidade"] =  quantidade
                    print(estoque)