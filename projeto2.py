from audioop import error

while True:
    opcao = input("Escolha uma operação (Soma, Subtração, Multiplicação, Divisão): ").upper()

    if opcao == "SOMA":
        print("Você escolheu a operação de Soma.")
        break
    elif opcao == "SUBTRACAO":
        print("Você escolheu a operação de Subtração.")
        break
    elif opcao == "MULTIPLICACAO":
        print("Você escolheu a operação de Multiplicação.")
        break
    elif opcao == "DIVISAO":
        print("Você escolheu a operação de Divisão.")
        break
    else:
        print("Operação inválida.")

a=float(input( "\nDigite o primeiro numero: "))
b=float(input( "\nDigite o segundo numero: "))
    
try:
    if opcao == "SOMA":
        resultado = a+b
        print(f"\n{resultado:.2f}\n")
        
    elif opcao =="SUBTRACAO":
        resultado = a-b
        print(f"\n{resultado:.2f}\n")
        
    elif opcao =="MULTIPLICACAO":
        resultado = a*b
        print(f"\n{resultado:.2f}\n")
        
    elif opcao =="DIVISAO":
        resultado = a/b
        print(f"\n{resultado:.2f}\n")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")