contas = []
soma = 0
for i in range(5):
    sla = float(input("selecione um valor: "))
    contas.insert(0,sla)
    soma = soma + sla
print(f"soma final: {soma}")