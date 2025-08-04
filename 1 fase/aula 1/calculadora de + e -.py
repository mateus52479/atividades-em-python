#8.	Faça um programa que peça para o usuário inserir dois números, pergunte se ele quer realizar a operação de adição ou de subtração e, que a partir desta escolha, mostre o resultado na tela.

n1 = float(input("primeiro numero: "))
n2 = float(input("segundo numero: "))
escolha = input("+ ou -: ")

if escolha == ("+"):
    print("resultado:" ,n1+n2)
elif escolha == ("-"):
    print("resultado: ", n1-n2)
else:
    print("coloque uma operação possivel")