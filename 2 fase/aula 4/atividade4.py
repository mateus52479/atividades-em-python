from time import sleep

lista_antiga = []
lista_atualizada = []

def adicionar(add):
    lista_atualizada.append(add)

def visualizar():
    print(lista_antiga)

def atualizar():
    lista_antiga.clear()
    for i in lista_atualizada:
        lista_antiga.append(i)

def excluir(tirar):
    if tirar in lista_antiga:
        lista_antiga.remove(tirar)
        print(f"contato '{tirar}' removida com sucesso!")
    else:
        print(f"contato '{tirar}' não encontrada na lista.")


while True:
    escolha = input("digite se deseja adicionar, visualizar, atualizar, excluir ou sair das contatos da lista: ")
    match escolha:
        case "adicionar":
            adesao = input("digite a nova contato para a lista: ")
            sleep(2)
            adicionar(adesao)
            print("contato adicionado com sucesso")
        
        case "visualizar":
            print("lista completa: ")
            visualizar()
            
        case "atualizar":
            atualizar()
            print("lista atualizada com sucesso")
            
        case "excluir":
            remove = input("digite o item que quer excluir: ")
            excluir(remove)

        case "sair":
            for i in range(3):
                print("saindo...")
                sleep(2)
            print("saida do programa com sucesso")
            break

        case _:
            print("opção invalida")        
