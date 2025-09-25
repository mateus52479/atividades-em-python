import math
lista = []

for i in range(2):
    cateto = float(input(f"digite o tamanho do {i+1}° cateto: "))
    lista.append(cateto)

def hipotenusa(cateto1, cateto2):
    hipo = math.hypot(cateto1, cateto2)
    return hipo
print(lista)

valor_final = hipotenusa(lista[0], lista[1])

print(f"valor da hipotenusa é: {valor_final}")