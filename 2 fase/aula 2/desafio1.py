biblioteca = {
    "nome1": {"autor": "joao", "ano": 1999},
    "nome2": {"autor": "rodrigo", "ano": 2022}
}

pesquisa = input("Digite o nome do livro: ")

if pesquisa in biblioteca:
    print(f"O autor: {biblioteca[pesquisa]['autor']}")
    print(f"O ano de publicação: {biblioteca[pesquisa]['ano']}")
else:
    print("Livro não encontrado na biblioteca.")