def funcao_linear():
    print("Bem-vindo ao assistente de Função Linear!")
    print("A forma da função é: f(x) = ax + b")
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))

    while True:
        print("\nO que deseja fazer?")
        print("1 - Calcular f(x) para um valor de x")
        print("2 - Encontrar a raiz da função (f(x) = 0)")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            x = float(input("Digite o valor de x: "))
            fx = a * x + b
            print(f"Para x = {x}, f(x) = {fx}")

        elif opcao == "2":
            if a == 0:
                print("A função não é linear, pois a = 0.")
            else:
                raiz = -b / a
                print(f"A raiz da função (onde f(x) = 0) é x = {raiz}")

        elif opcao == "3":
            print("Encerrando o programa. Até mais!")
            break

        else:
            print("Opção inválida, tente novamente.")
funcao_linear()