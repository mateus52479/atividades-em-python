nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))

if idade >= 0 and idade <=2:
    print(f"o usuario {nome} tem escolaridade de nivel berçario")
elif idade >= 3 and idade <=6:
    print(f"o usuario {nome} tem escolaridade de nivel educação infantil")
elif idade >= 7 and idade <=10:
    print(f"o usuario {nome} tem escolaridade de nivel ensino fundamental I")
elif idade >= 11 and idade <=15:
    print(f"o usuario {nome} tem escolaridade de nivel ensino fundamental II")
elif idade >= 16 and idade <=18:
    print(f"o usuario {nome} tem escolaridade de nivel ensino medio")
else:
    print(f"{nome}, nao possuimos informações pra sua idade")