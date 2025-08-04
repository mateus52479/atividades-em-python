valor = int(input("digite seu numeral: "))
divisao = 0

for i in range(1, valor +1):
    if valor % i == 0:
        divisao +=1
print(divisao)

if divisao == 2:
    print(f"seu numeral {valor} é primo")
else:
    print(f"seu numeral {valor} não é primo")