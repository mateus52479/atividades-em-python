def selecionar_destino():
    destinos = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Recife"]
    print("Destinos disponíveis:")
    for i, destino in enumerate(destinos, 1):
        print(f"{i}. {destino}")
    
    while True:
        try:
            escolha = int(input("Escolha o número do destino desejado: "))
            if 1 <= escolha <= len(destinos):
                return destinos[escolha - 1]
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


def selecionar_data():
    while True:
        data = input("Digite a data da viagem (formato: DD/MM/AAAA): ")
        if validar_data(data):
            return data
        else:
            print("Data inválida. Tente novamente.")


def validar_data(data):
    from datetime import datetime
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def selecionar_passageiros():
    while True:
        try:
            numero = int(input("Digite o número de passageiros: "))
            if numero > 0:
                return numero
            else:
                print("Número deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def confirmar_reserva(destino, data, passageiros):
    print("\n--- Resumo da Reserva ---")
    print(f"Destino: {destino}")
    print(f"Data: {data}")
    print(f"Número de passageiros: {passageiros}")
    
    confirmacao = input("Deseja confirmar a reserva? (s/n): ").strip().lower()
    if confirmacao == 's':
        print("Reserva confirmada! Obrigado por usar nosso sistema.")
    else:
        print("Reserva cancelada.")


def iniciar_reserva():
    print("=== Bem-vindo ao Sistema de Reservas Aéreas ===")
    
    destino = selecionar_destino()
    data = selecionar_data()
    passageiros = selecionar_passageiros()
    
    confirmar_reserva(destino, data, passageiros)


# Executa o programa
if __name__ == "__main__":
    iniciar_reserva()
