#7.	Faça um programa que peça para o usuário inserir dois números e que verifique qual é o maior ou se eles são iguais.

n1 = float(input("adicione o primeiro numero: "))
n2 = float(input("adicione o segundo numero: "))

if n1 > n2:
    print(f"o numero {n1} é maior que o numero {n2}")
elif n1 <  n2:
    print(f"o numero {n2} é maior que o numero {n1}")
else:
    print("os numeros sao iguis")