altura_lista_todos = []
altura_lista_mulheres = []
altura_lista_homens = []

for i in range(10):
   while True:
        altura = float(input("digite a sua altura: "))
        genero = input("digite o seu genero (masculino ou feminino): ").lower()
        altura_lista_todos.append(altura)

        if genero == "feminino":
            altura_lista_mulheres.append(altura)
            break

        elif genero == "masculino":
            altura_lista_homens.append(altura)
            break

        else:
            print("digite uma opção possivel")

print(f"\n maior altura do grupo: {max(altura_lista_todos)} \n menor altura do grupo: {min(altura_lista_todos)}")
print(f"\n média de altura das mulheres: {sum(altura_lista_mulheres)/(len(altura_lista_mulheres)):.2}")
print(f"\n a quantidade de homens: {len(altura_lista_homens)}")
print(f"\n a porcentagem de homens: {(len(altura_lista_homens)*100)/len(altura_lista_todos)}% \n a porcentagem de mulheres: {(len(altura_lista_mulheres)*100)/len(altura_lista_todos)}%")
