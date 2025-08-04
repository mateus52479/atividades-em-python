#Faça um programa que receba como entrada os dados de um funcionário: nome, número de horas trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E ao final mostrar seu nome e salário final calculado.

nome = input("digite seu nome: ")
nht = float(input("numero de horas trabalhadas: "))
vht = float(input("valor de horas trabalhadas: "))

tudin = nht * vht

desconto = tudin - (tudin*2/100)

print(f" valor do salario bruto: {tudin} \n valor do salario liquido: {desconto}")