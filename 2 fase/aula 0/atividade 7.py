nome = input("digite seu nome: ")
altura = float(input("digite sua altura: "))
peso = float(input("digite seu peso: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"{nome}, sua situação é abaixo do peso")
    
elif imc >= 18.5 and imc < 25:
    print(f"{nome}, sua situação é peso normal")

elif imc >= 25 and imc < 30:
    print(f"{nome}, sua situação é acima do peso")
else:
    print(f"{nome}, sua situação é de obesidade")
