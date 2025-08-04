soma = 0
lista = []
while True:
    n = int(input("digite um numeral"))
    if n <= -1:
        break
    else:
        lista.append(n)
        soma+=n
        media = soma/len(lista)
print(max(lista))
print(min(lista))
print(media)
print(soma)
