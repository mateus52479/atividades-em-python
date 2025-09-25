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
        print(f"Tarefa '{tirar}' removida com sucesso!")
    else:
        print(f"Tarefa '{tirar}' não encontrada na lista.")


while True:
    escolha = input("digite se deseja adicionar, visualizar, atualizar, excluir ou sair das tarefas da lista: ")
    match escolha:
        case "adicionar":
            adesao = input("digite a nova tarefa para a lista: ")
            sleep(2)
            adicionar(adesao)
            print("atividade adicionada com sucesso")
        
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
