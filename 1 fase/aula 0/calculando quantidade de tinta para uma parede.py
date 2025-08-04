# Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².

altura = float(input("digite a altura da parede: "))
largura = float(input("digite a largura da parede: "))

area = altura * largura
tinta = area / 2

print(f"area da parede: {area} \n quantidade de balde: {tinta}")