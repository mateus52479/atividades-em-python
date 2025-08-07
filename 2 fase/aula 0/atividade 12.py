nome = input("digite nome do cliente: ")
idade = int(input("digite a idade do cliente: "))
Vplano = float(input("informe o valor do plano de saude: "))

if idade >= 0 and idade <=18:
    Vfinal = Vplano + (Vplano * 0.05)
elif idade >= 19 and idade <=35:
    Vfinal = Vplano + (Vplano * 0.10)
elif idade >= 36 and idade <=60:
    Vfinal = Vplano + (Vplano * 0.15)
else:
    Vfinal = Vplano + (Vplano * 0.20)

print(f"o valor final do plano é {Vfinal}")