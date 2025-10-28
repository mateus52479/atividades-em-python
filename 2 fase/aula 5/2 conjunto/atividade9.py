from math import sqrt, sin, ceil, floor

#atividade A
numero_positivo = float(input("digite um numero positivo: "))
raiz = lambda x: sqrt(x)
print(f"a raiz de {numero_positivo} é {raiz(numero_positivo)}")

#atividade B
numero_angulo = float(input("digite um angulo qualquer: "))
seno = lambda x: sin(x)
print(f"o valor do seno de {numero_angulo} é {sin(seno)}")


#atividade C
numero_arrendondado = float(input("digite um numero decimal qualquer: "))
cima = lambda x: ceil(x)
baixo = lambda x: floor(x)
print(f"o valor arredondado para cima de {numero_arrendondado} é {cima(numero_arrendondado)}")
print(f"o valor arredondado para baixo de {numero_arrendondado} é {baixo(numero_arrendondado)}")