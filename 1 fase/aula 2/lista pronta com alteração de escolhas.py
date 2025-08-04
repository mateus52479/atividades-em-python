filmes = ["ação", "aventura"]
jogos = ["fps", "fazenda"]
livros = ["romance", "suspense"]
esporte = ["futebol", "golf"]

conjunto = filmes + jogos + livros + esporte
print(conjunto)

escolha_livro = input("escolha um estilo de livro entre romance(1) e suspense(2): ")
escolha_esporte = input("escolha um a remover futebol(1) ou golf(2): ")

if escolha_livro == 1:
    print("livro escolhido: ",livros[0])
else:
    print("livro escolhido: ",livros[1])


if escolha_esporte == 1:
    esporte.remove("futebol")
    print("como finalizou a lista: ", esporte)
else:
    esporte.remove("golf")
    print("como finalizou a lista: ", esporte)