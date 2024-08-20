nome = input ("Escreva o seu nome: \n")
idade = float (input ("Escreva sua idade: \n"))
altura = float(input ("Escreva sua altura em 'm': \n"))
peso=float (input("Escreva seu peso: \n"))
imc = peso/(altura ** 2)
print(f"\n{nome}, seu IMC é: {imc:.2f}")
if imc < 16.9:
    {
        print("Muito abixo do peso")
    }
elif 17<= imc <=18.4:
    {
        print("Abaixo do peso")
    }
elif 18.5<= imc <=24.9:
    {
        print("Peso normal")
    }
elif 25<= imc <=29.9:
    {
        print("Acima do peso")
    }
elif 30<= imc <=34.9:
    {
        print("Obseidade grau I")
    }
elif 35<= imc <=40:
    {
        print("Obesidade grau II")
    }
else:
    {
        print("Obesidade grau III")
    }