while True:
    opcao = input("Escolha uma operação (Soma, Subtracao, Multiplicacao, Divisao): ").upper()

    if opcao in ["SOMA", "SUBTRACAO", "MULTIPLICACAO", "DIVISAO"]:
        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")
            continue  # Reinicia o loop se a entrada for inválida

        try:
            if opcao == "SOMA":
                resultado = a + b
                print(f"\nResultado da soma: {resultado:.2f}\n")
                
            elif opcao == "SUBTRACAO":
                resultado = a - b
                print(f"\nResultado da subtração: {resultado:.2f}\n")
                
            elif opcao == "MULTIPLICACAO":
                resultado = a * b
                print(f"\nResultado da multiplicação: {resultado:.2f}\n")
                
            elif opcao == "DIVISAO":
                resultado = a / b
                print(f"\nResultado da divisão: {resultado:.2f}\n")
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida.")
        
        break  # Sai do loop após realizar a operação
    else:
        print("Operação inválida. Tente novamente.")
