nome = input ("Escreva o seu nome: \n")
idade = float (input ("Escreva sua idade: \n"))
altura = float(input ("Escreva sua altura em 'm': \n"))
peso=float (input("Escreva seu peso: \n"))
imc = peso/(altura ** 2)

print(f"\n{nome}, seu IMC é: {imc:.2f}")

if idade <18: 
    if imc < 16:
        {
            print("Muito abixo do peso\n")
        }
    elif 16<= imc <=18.4:
        {
            print("Abaixo do peso\n")
        }
    elif 18.5<= imc <=23.9:
        {
            print("Peso normal\n")
        }
    elif 24<= imc <=28.9:
        {
            print("Sobrepeso\n")
        }
    elif 29<= imc <=32.9:
        {
            print("Obseidade grau I\n")
        }
    elif 33<= imc <=37.9:
        {
            print("Obseidade grau II\n")
        }
    else:
        {
            print("Obesidade grau III\n")
        }
      
elif 18 <= idade <=24:
    if imc < 18.5:
        {
            print("Abaixo do peso\n")
        }
    elif 18.5<= imc <=24.9:
        {
            print("Peso nomal\n")
        }
    elif 25<= imc <=29.9:
        {
            print("Sobrepeso\n")
        }
    elif 30<= imc <=34.9:
        {
            print("Obseidade grau I\n")
        }
    elif 35<= imc <=39.9:
        {
            print("Obseidade grau II\n")
        }
    else:
        {
            print("Obesidade grau III\n")
        }
elif 25<= idade <=34:
    if imc < 19:
        {
            print("Abixo do peso\n")
        }
    elif 19<= imc <=25.9:
        {
            print("Peso normal\n")
        }
    elif 26<= imc <=30.9:
        {
            print("Sobrepeso\n")
        }
    elif 31<= imc <=35.9:
        {
            print("Obseidade grau I\n")
        }
    elif 36<= imc <=40.9:
        {
            print("Obseidade grau II\n")
        }
    else:
        {
            print("Obesidade grau III\n")
        }
else:
    if imc < 20:
        {
            print("Abixo do peso\n")
        }
    elif 20<= imc <=26.9:
        {
            print("Peso normal\n")
        }
    elif 27<= imc <=31.9:
        {
            print("Sobrepeso\n")
        }
    elif 32<= imc <=36.9:
        {
            print("Obseidade grau I\n")
        }
    elif 37<= imc <=41.9:
        {
            print("Obseidade grau II\n")
        }
    else:
        {
            print("Obesidade grau III\n")
        }