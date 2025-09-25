from time import sleep

lista = []


def adicionar(add):
    lista.append(add)

def visualizar():
    print(lista)

# def alterar():
#     lista.clear()
#     for i in lista:
#         lista.append(i)

def excluir(tirar):
    if tirar in lista:
        lista.remove(tirar)
        print(f"Tarefa '{tirar}' removida com sucesso!")
    else:
        print(f"Tarefa '{tirar}' não encontrada na lista.")

# def calculo():
#     sum(lista)


while True:
    escolha = input("digite se deseja adicionar, alterar, excluir, exibir, calcular media ou sair das tarefas da lista: ")
    match escolha:
        case "adicionar":
            adesao = input("digite a nova tarefa para a lista: ")
            sleep(2)
            adicionar(adesao)
            print("atividade adicionada com sucesso")
        
        # case "alterar":
        #     alterar()
            
        case "excluir":
            remove = input("digite a nota que quer excluir: ")
            excluir(remove)
            
        case "exibir":
            print("todas as notas: ")
            visualizar()

        # case "calcular media":
        #     calculo()
        

        case "sair":
            for i in range(3):
                print("saindo...")
                sleep(2)
            print("saida do programa com sucesso")
            break

        case _:
            print("opção invalida")        
