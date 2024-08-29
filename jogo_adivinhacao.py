import random

# Define o número secreto aleatório
numero_secreto = random.randint(1, 100)
tentativas_restantes = 10

print("\nVocê tem 10 tentativas para adivinhar o número secreto entre 1 e 100.")

while tentativas_restantes > 0:
    try:
        # Solicita ao usuário um palpite
        palpite = int(input("Digite seu palpite: "))
        
        # Verifica se o palpite está correto
        if palpite == numero_secreto:
            print("\nParabéns! Você adivinhou o número secreto!")
            break
        elif palpite < numero_secreto:
            print("\nO número secreto é maior.")
        else:
            print("\nO número secreto é menor.")
        
        # Diminui o número de tentativas restantes
        tentativas_restantes -= 1
        print(f"Tentativas restantes: {tentativas_restantes}\n")
        
    except ValueError:
        print("\nPor favor, insira um número válido.\n")

if tentativas_restantes == 0:
    print(f"Você perdeu! O número secreto era {numero_secreto}.")
