lista = []

while True:
    n = int(input("digite qualquer numero diferente de zero (caso 0 fecha o programa): "))
    if n != 0:
        lista.append(n)
    else:
        break

numero = int(input("digite um numero: "))

def listagem():
    if numero in lista:
        return True
    return False

print(f"numero contido na lista: {listagem()}")