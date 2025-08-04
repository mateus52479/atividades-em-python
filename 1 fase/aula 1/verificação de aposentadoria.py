#15.	Leia a idade e o tempo de servico de um trabalhador e escreva se ele pode ou nao se aposentar. As condições para aposentadoria são:

idade = float(input("digite sua idade: "))
work = float(input("digite seu tempo de contribuição: "))

if idade >= 65 or work >= 30:
    print("voce ja pode se aposentar yaaaay")
elif idade >= 65 and work >= 25:
    print("voja pode em")
else:
    print("ainda nao amigo, ainda nao")