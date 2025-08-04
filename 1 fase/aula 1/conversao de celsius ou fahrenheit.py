#11.	Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida conversão.

pergunta = float(input("qual conversao gostaria de fazer celsius->fahrenheit(1) ou fahrenheit->celsius(2): "))
numero = float(input("digite a temperatura: "))

if pergunta == 1:
    print("resultado:", numero * 1.8 +32)
elif pergunta == 2:
    print("resultado:", (numero - 32)/1,8) 