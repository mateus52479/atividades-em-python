def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida! Digite um número.")


while True:
    print("\n--- Calculadora ---")
    print("Escolha uma operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potenciação")
    print("0 - Sair")

    escolha = input("Digite a opção desejada: ")

    match escolha:
        case "1":
            n1 = ler_numero("Digite o primeiro número: ")
            n2 = ler_numero("Digite o segundo número: ")
            resultado = lambda x, y: x + y
            print(f"Resultado: {resultado(n1, n2)}")

        case "2":
            n1 = ler_numero("Digite o primeiro número: ")
            n2 = ler_numero("Digite o segundo número: ")
            resultado = lambda x, y: x - y
            print(f"Resultado: {resultado(n1, n2)}")

        case "3":
            n1 = ler_numero("Digite o primeiro número: ")
            n2 = ler_numero("Digite o segundo número: ")
            resultado = lambda x, y: x * y
            print(f"Resultado: {resultado(n1, n2)}")

        case "4":
            n1 = ler_numero("Digite o primeiro número: ")
            n2 = ler_numero("Digite o segundo número: ")
            resultado = lambda x, y: x / y
            print(f"Resultado: {resultado(n1, n2)}")

        case "5":
            n1 = ler_numero("Digite a base: ")
            n2 = ler_numero("Digite o expoente: ")
            resultado = lambda x, y: x ** y
            print(f"Resultado: {resultado(n1, n2)}")

        case "0":
            print("Saindo da calculadora... Até mais!")
            break

        case _:
            print("Opção inválida! Tente novamente.")
