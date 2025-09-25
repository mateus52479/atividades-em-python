estoque = {"caneta" : (2.50, 10), "caderno" : (15.00, 5), "borracha" : (1.00, 20)}

produto = input("digite o nome do produto: ")

money, quantidade = estoque.get(produto)
print(f"valor total em estoque: {quantidade*money}")