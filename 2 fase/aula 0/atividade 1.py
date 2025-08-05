money = float(input("digite a quantidade de renda por hora: "))
time = float(input("digite o numero de horas trabalhadas no mês: "))

bruto = money * time
inss = (bruto * 0.11)
imposto = (bruto * 0.08)
sindicato = (bruto * 0.05)
total = bruto - (sindicato + imposto + inss)
print(f"valor bruto: {bruto}")
print(f"valor retirado do inss: {inss}")
print(f"valor retirado do imposto: {imposto}")
print(f"valor retirado do sindicato: {sindicato}")
print(f"valor liquido: {total}")