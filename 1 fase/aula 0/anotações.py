a = 6
b = 7.8
c = "mateus"
d = True

#visualizando os tipos de variaveis
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(a)
print("hello world!")

valor = 1
print("o valor digitado foi:", valor)

#outra forma
print(f"oi {c}, o valor digitado foi de {valor} reais")

#imput

nome = input("digite seu nome: ")
idade = input("digite sua idade: ")

print(f"oi {nome}, parabéns pelos {idade} anos")

#exercicios

valor1 = float(input("digite um valor: "))
valor2 = float(input("digite outro valor: "))

soma = valor1**valor2
print(f"oiii, seu valor deu exatamnete {soma}")

#operadores

a = 7
b = 2

soma = a+b
mult = a*b
pota = a**b
potb = b**a
div = a/b
divr = a//b
porcem = a%b

print(f"resultados: \n soma: {soma} \n multiplicação: {mult} \n potencia do a: {pota} \n potencia do b: {potb} \n divisão: {div} \n divisão resto zero: {divr} \n resto da divisão: {porcem}" )