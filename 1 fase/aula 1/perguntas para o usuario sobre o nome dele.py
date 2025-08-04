#1.	Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

input("opá, qual é o seu nome? ")
perg = input("você gosta dele? ")

if perg == ("sim" or "SIM"):
    print("aah que bom")

elif perg == ("nao" or "NAO"):
    print("po que triste entao")

else:
    print("nao intendi")
    