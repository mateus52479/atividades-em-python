lista = []



while True:
    comando = input("digite um comando:\n1-adicionar tarefa\n2-remover uma tarefa\n3-exibir tarefas\n4-buscar tarefa\n5-sair\n")
    print("-"*192)
    match comando:
        case "1":
            tarefa = input("digite a nova tarefa: ")
            lista.append(tarefa)
            print("-"*192)

        case "2":
            print(lista)
            remover = input("digite qual termo da lista remover:")
            lista.remove(remover)
            print("-"*192)
        
        case "3":
            print("lista de tarefas:\n")
            for i in lista:
                print(i)
            print("-"*192)
        
        case "4":
            procurar = input("digite a tarefa que você gostaria de procurar: ")
            if lista[procurar] == procurar:
                print("tarefa existente")
            else:
                print("tarefa nao incontrada")
            print("-"*192)
        
        case "5":
            print("saindo....")
            break