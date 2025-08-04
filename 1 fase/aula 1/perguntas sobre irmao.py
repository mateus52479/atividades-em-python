# 5.	Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.

irmaos = input("você possui irmaos? ")

if irmaos == ("sim" or "SIM"):
    input("que legal, quantos? ")
    print("legal eu acho")
elif irmaos == ("nao" or "NAO"):
    input("gostaria de ter? ")
    print("maneirão")
else:
    print("o amigo me fala uma coisa certa na vida")
    