lista = []
for i in range(10):
    notas = float(input("insira sua media: "))
    if notas >= 7:
        lista.append(notas)
print(lista)
print(f"alunos aprovados: ", len(lista))