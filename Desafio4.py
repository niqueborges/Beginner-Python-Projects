# Calculo de IMC - Indice de Massa Corporal

''' 
Menor que 18.5: Abaixo do Peso
Entre 18.5 e 24.9: Peso Normal
Entre 25 e 29.9: Sobrepeso
Entre 30 e 39.9: Obesidade Grau 1
Acima de 40: Obesidade Grau 2

'''
altura = float(input('Qual é a sua Altura em cm? '))
peso = float(input('Qual é o seu Peso em kg? '))

IMC = peso / (altura/100)**2

if IMC < 18.5:
    print(f'Seu IMC é {IMC:.2f} e você está abaixo do peso.')
elif 18.5 <= IMC <= 24.9:
    print(f'Seu IMC é {IMC:.2f} e você está com o peso normal.')
elif 25 <= IMC <= 29.9:
    print(f'Seu IMC é {IMC:.2f} e você está com sobrepeso.')
elif 30 <= IMC <= 39.9:
    print(f'Seu IMC é {IMC:.2f} e você está com obesidade grau 1.')
else:
    print(f'Seu IMC é {IMC:.2f} e você está com obesidade grau 2.')




    
