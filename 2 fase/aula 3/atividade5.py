n1 = int(input("digite o 1° numero: "))
n2 = int(input("digite o 2° numero: " ))
limite = int(input("digite um limite para 1° e o 2° numero: "))

def soma_limitada():
    if (n1 + n2) > limite: 
        return True
    return False

print(f"limitação ultrapassada: {soma_limitada()}")