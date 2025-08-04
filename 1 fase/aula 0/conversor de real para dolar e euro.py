# Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para Euros.

nome = input("digite seu nome: ")
money = float(input("digite sua renda: "))

dolar = money /5.41
euro = money /6.19 

print(f"olá {nome},seu conversão em: \n dolar: {dolar} \n euro: {euro}")