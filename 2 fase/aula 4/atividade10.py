#atividade A
from random import randint

numero = randint(1, 100)
print(f"numero sorteado {numero}")

#atividade B
from random import choice

nomes = ("Mateus", "Renata", "Dimitre")
print(f"nome escolhido: {choice(nomes)}")

#atividade C
from random import shuffle

numeros = [1, 2, 3, 4, 5]
shuffle(numeros)
print(f"lista embaralhada: {numeros}")
