numero = int(input("digite um numero inteiro positivo: "))

def soma_numeros():
    somatorio = 0
    for i in range(numero+1):
        somatorio += i
    return somatorio

todos_numeros = soma_numeros()

print(f"a soma de todos os numeros de 0 a {numero} é {todos_numeros}")