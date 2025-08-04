#13.	Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos.

n1 = float(input("digite a primeira nota (max 5): "))
n2 = float(input("digite a segunda nota (max 5): "))
n3 = float(input("digite a terceira nota: "))

media = (n1 + n2 + n3)/2 

if media >= 6:
    print("parabens você passou com média: ",media)
else:
    print("que pena parece que você reprovou com média: ",media)

