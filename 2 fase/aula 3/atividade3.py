nome = input("digite seu nome: ")


def funcionario():
    salario = input("digite seu salario: ")
    if salario == "":
        salario = 9000
    return salario

empregado = funcionario()

print(f"{nome} voce possui um salario de {empregado}")