alln = []
caixa_par = []
caixa_impar = []
for i in range(20):
    n = int(input("digite 20 numeros: "))
    alln.append(n)
    if n % 2 == 0:
        caixa_par.append(n)
    else: 
        caixa_impar.append(n)
print(f"todos os numeros: {alln}")        
print(f"numeros pares: {caixa_par}")
print(f"numeros impares: {caixa_impar}")
 