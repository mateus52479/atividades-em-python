from functools import reduce

lista = [2, 3, 5, 6, 7, 8]

mutiplicacao = reduce(lambda x, y: x * y, lista)
print(mutiplicacao)