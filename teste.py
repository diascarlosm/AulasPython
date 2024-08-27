while True:
    opcao = input("Escolha uma operação (+, -, *, /): ").upper()

    if opcao == "+":
        print("Você escolheu a operação de Soma.")
        break
    elif opcao == "-":
        print("Você escolheu a operação de Subtração.")
        break
    elif opcao == "*":
        print("Você escolheu a operação de Multiplicação.")
        break
    elif opcao == "/":
        print("Você escolheu a operação de Divisão.")
        break
    else:
        print("Operação inválida.")

# Solicitação do primeiro número com validação
while True:
    try:
        a = float(input("\nDigite o primeiro número: "))
        break
    except ValueError:
        print("Entrada inválida! Por favor, insira um número válido.")

# Solicitação do segundo número com validação
while True:
    try:
        b = float(input("\nDigite o segundo número: "))
        break
    except ValueError:
        print("Entrada inválida! Por favor, insira um número válido.")

try:
    if opcao == "+":
        resultado = a + b
        print(f"\n{resultado:.2f}\n")
    elif opcao == "-":
        resultado = a - b
        print(f"\n{resultado:.2f}\n")
    elif opcao == "*":
        resultado = a * b
        print(f"\n{resultado:.2f}\n")
    elif opcao == "/":
        resultado = a / b
        print(f"\n{resultado:.2f}\n")
except ZeroDivisionError:
    print("\nErro: Divisão por zero não é permitida.\n")
