import math

escolha = input("digite se deseja calcular a area de um cirulo, retangulo ou triangulo:")

def circuferencia(raio):
    area = math.pi * math.pow(raio, 2)
    return area

def retangulo(altura, base):
    area = altura * base
    return area


match escolha:
    case "circulo":
        raios = float(input("digite o tamanho do raio: "))
        resultado = circuferencia(raios)
        print(f"tamanho da area da circuferencia é: {resultado:.3}")

    case "retangulo":
        alturas = float(input(f"digite a altura do retangulo: "))
        bases = float(input("digite o tamanho da base: "))
        resultado = retangulo(alturas, bases)
        print(f"tamanho da area do retangulo é: {resultado}")
    case "triangulo":
        alturas = float(input(f"digite a altura do triangulo: "))
        bases = float(input("digite o tamanho da base: "))
        resultado= retangulo(alturas, bases)
        print(f"tamanho da area do triangulo é: {resultado/2:.3}")
