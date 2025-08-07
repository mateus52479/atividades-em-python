candidato1 = 0
candidato2 = 0
candidato3 = 0

nvotos = int(input("digite a quantidade de votos totais: "))

for i in range(nvotos):
    while True:
        voto = input("voce quer votar no canditato 1, 2 ou 3? ")

        if voto == "1":
            candidato1 += 1
            break

        elif voto == "2":
            candidato2 += 1
            break

        elif voto == "3":
            candidato3 += 1
            break

        else:
            print("voto digitado automaticamente, reescreva o seu voto: ")

print(f"\nresultado final: \ncandidato 1: {candidato1} \ncandidato 2: {candidato2} \ncandidato 3: {candidato1}")