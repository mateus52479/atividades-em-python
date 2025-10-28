from math import hypot
lista = []

for i in range(2):
    cateto = float(input(f"digite o tamanho do {i+1}° cateto: "))
    lista.append(cateto)

hipotenusa = lambda x,y: hypot(x, y) 

print(f"valor da hipotenusa é: {hipotenusa(lista[0], lista[1])}")