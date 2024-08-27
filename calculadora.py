# Função para escolher a operação matemática
def escolher_operacao():
    while True:
        # Solicita ao usuário que escolha uma operação e converte a entrada para maiúsculas
        opcao = input("\nEscolha uma operação (Soma, Subtração, Multiplicação, Divisão): ").upper()
        # Verifica se a opção escolhida é válida
        if opcao in ["SOMA", "SUBTRACAO", "MULTIPLICACAO", "DIVISAO"]:
            print(f"Você escolheu a operação de {opcao.capitalize()}.")
            return opcao
        else:
            print("Operação inválida!")

# Função para solicitar um número do usuário com validação de entrada
def solicitar_numero(mensagem):
    while True:
        try:
            # Tenta converter a entrada do usuário para um número float
            return float(input(mensagem))
        except ValueError:
            # Exibe uma mensagem de erro se a conversão falhar
            print("\nEntrada inválida! Por favor, insira um número válido.")

# Função para realizar o cálculo baseado na operação escolhida
def calcular(opcao, a, b):
    while True:
        try:
            # Realiza a operação matemática escolhida pelo usuário
            if opcao == "SOMA":
                return a + b
            if opcao == "SUBTRACAO":
                return a - b
            if opcao == "MULTIPLICACAO":
                return a * b
            elif opcao == "DIVISAO":
                return a / b
        except ZeroDivisionError:
            # Trata o erro de divisão por zero
            print("Erro: Divisão por zero não é permitida.\n")
            return None

# Função principal que coordena a execução do programa
def main():
    # Solicita ao usuário a operação desejada
    opcao = escolher_operacao()
    # Solicita os números para o cálculo
    a = solicitar_numero("\nDigite o primeiro número: ")
    b = solicitar_numero("\nDigite o segundo número: ")
    # Realiza o cálculo com os números fornecidos e a operação escolhida
    resultado = calcular(opcao, a, b)
    
    # Verifica se houve um resultado válido e exibe o resultado
    if resultado is not None:
        print(f"\nResultado: {resultado:.2f}\n")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()

# Função para solicitar um número, agora com verificação adicional para divisão por zero
def solicitar_numero(mensagem, opcao=None):
    while True:
        try:
            num = float(input(mensagem))
            # Verifica se a operação é uma divisão e se o número é zero
            if opcao == "DIVISAO" and num == 0:
                print("Erro: Divisão por zero não é permitida. Por favor, insira outro número.")
            else:
                return num
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido.")

# Função para realizar o cálculo com verificação de divisão por zero e impressão do resultado
def calcular(opcao, a, b):
    try:
        if opcao == "SOMA":
            print(f"{a} + {b} = {a+b}")
            return a + b
        if opcao == "SUBTRACAO":
            print(f"{a} - {b} = {a-b}")
            return a - b
        if opcao == "MULTIPLICAO":
            print(f"{a} * {b} = {a*b}")
            return a * b
        elif opcao == "DIVISAO":
            print(f"{a} / {b} = {a/b}")
            return a / b
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.\n")
        return None
