notas = {
 "Ana": [7, 8, 9],
 "Carlos": [6, 5, 7]
}

for i in notas:
    print(f"o aluno {i} está com {sum(notas[i])/3} de media")