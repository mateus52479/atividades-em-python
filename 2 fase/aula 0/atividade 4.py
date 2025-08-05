name = input("digite seu nome: ")
idade = int(input("digite seu idade: "))
peso = float(input("digite seu peso: "))

if idade <= 15:
    print("idade insuficiente para doação de sangue")
elif (idade == 16 or idade == 17) and (peso >= 55):
    print("parabéms, você poder ajudar doando sangue")
elif (idade >= 18 and idade == 69) and (peso >= 60):
    print("parabéms, você poder ajudar doando sangue")
else:
    print("você não pode doar sangue")