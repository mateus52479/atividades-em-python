#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. 

preco = float(input("digite o valor do produto: "))

descontado = preco-(preco*5/100)

print(descontado)