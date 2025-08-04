lista = []
for i in range(3):
    idade = int(input("digite a sua idade: "))
    altura = float(input("digite a sua altura: "))
    if idade >= 13 and altura < 1.42:
        lista.append(altura)
print(len(lista))