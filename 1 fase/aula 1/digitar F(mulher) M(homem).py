#1.	Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
sigla = input("digite F para feminino ou M para masculino: ").upper()

if sigla == "F":
    print("ola moça")
elif sigla == "M":
    print("ola moço")
else:
    print("escreva uma opção possivel")