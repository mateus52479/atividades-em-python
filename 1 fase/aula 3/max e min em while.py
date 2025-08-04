i = 1
numeros = []
while i <=10:
    n=int(input("digite seus numeros: "))
    numeros.append(n)
    i+=1
print(f"todos os seus numeros: {numeros}")
print(f"seu maior numero: {max(numeros)}")
print(f"seu menor numero: {min(numeros)}")