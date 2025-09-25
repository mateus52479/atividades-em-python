from random import randint

def aleatoridade():
    numero = randint(1,100)
    return numero

def jogo():
    while True:
        chute = int(input("digite qual numero vc acha que é: "))
        if chute == numeral:
            print("voce ganhou o jogo!!!!")
            break
        elif chute <= numeral:
            print("o seu numero é menor que o numero sorteado")
        else:
            print("o seu numero é maior que o numero sorteado")
  
numeral = aleatoridade()
jogo()




