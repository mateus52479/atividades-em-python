from math import pi, pow

escolha = input("digite se deseja calcular a area de um cirulo, retangulo ou triangulo: ")

match escolha:
    case "circulo":
        raios = float(input("digite o tamanho do raio: "))
        resultado = lambda x: pi * pow(x, 2)
        print(f"tamanho da area da circuferencia é: {resultado(raios):.3}")

    case "retangulo":
        alturas = float(input(f"digite a altura do retangulo: "))
        bases = float(input("digite o tamanho da base: "))
        resultado = lambda x,y: x * y 
        print(f"tamanho da area do retangulo é: {resultado(alturas, bases)}")
        
    case "triangulo":
        alturas = float(input(f"digite a altura do triangulo: "))
        bases = float(input("digite o tamanho da base: "))
        resultado= resultado = lambda x,y: x * y /2 
        print(f"tamanho da area do triangulo é: {resultado(alturas, bases)}")
