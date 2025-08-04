numero = int(input("digite o numero à fatorar: "))
antecessor = numero

while antecessor>1:
    numero *= (antecessor-1)
    antecessor -= 1
print(numero)