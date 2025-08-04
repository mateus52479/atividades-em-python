# Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo.

n = float(input("digite seu numero: "))

if n < 0:
    print(f"o numero {n} é negativo" )

elif n > 0:
        print(f"o numero {n} é positivo" )
else:
    print(f"o numero {n} é nulo" )