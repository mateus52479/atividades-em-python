nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))

if (idade > 65 or idade == 16 or idade == 17):
    print(f"{nome}, você é um eleitor facultativo, caso queira votar poderá!")

elif idade >=18:
    print(f"{nome}, você é um eleitor obrigatorio, é obrigado a votar")

else: 
    print(f"{nome}, você não é um eleitor, não podera votar")