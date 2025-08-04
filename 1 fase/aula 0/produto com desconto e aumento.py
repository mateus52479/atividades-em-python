# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15% de aumento.

preco = float(input("digite o preço do produto: "))

desconto = preco - (preco*5/100)
aumento = desconto + (desconto*15/100)

print(f" preço final: {aumento} ")