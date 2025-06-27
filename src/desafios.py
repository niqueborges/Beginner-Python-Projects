# Cálculo da área de um círculo
raio = 4
pi = 3.14
print(f"Área do círculo:' "+str(pi*raio**2))

print('---')

#Cálculo da área de um retângulo#
base = 2
largura = 3
print(f"Área do retângulo: "+str(base*largura))

print('---'
      
      # Desafio com if, elif e else

'''
Criar um programa que dependendo da temperatura (em celsius) do steak ele retorna o ponto do cozimento 
em português. O usuário deve informar a temperatura do steak.

Temperaturas - Cozimento
120°F ou 48°C - Rare (Selada)
130°F ou 54°C - Medium Rare (Ao ponto para mal)
140°F ou 60°C - Medium (Ao ponto)
150°F ou 65°C - Medium Well (Bem ao ponto)
160°F ou 71°C - Well Done (Bem passada)
'''

tem_celsius = float(input('Qual a temperatura do steak em celsius? '))

if tem_celsius < 48:
    print('Cozinhar mais')
elif tem_celsius in range(48, 53):
    print('Rare (Selada)')
elif tem_celsius in range(54, 59):  
    print('Medium Rare (Ao ponto para mal)')
elif tem_celsius in range(60, 64):
    print('Medium (Ao ponto)')
elif tem_celsius in range(65, 70):
    print('Medium Well (Bem ao ponto)')
else:
    print('Well Done (Bem passada)')

# Fim)

print('---')

# Desafio com funções

'''
Criar um programa que calcula a quantidade de tintas necessárias para pintar uma parede. 
O usuário deve informar as seguintes informações: Rendiment, altura e largura.
O programa deve mostrar na tela a mensagem: 'Você necessita de x latas de tinta para pintar a parede.'
'''

rendimento = float(input('Qual o rendimento da tinta em m² por litro? '))
altura = float(input('Qual a altura da parede em metros? '))
largura = float(input('Qual a largura da parede em metros? '))

def calcula_tinta(rendimento, altura, largura):
    area = altura * largura
    tinta = area / rendimento
    return tinta

print(f'Você necessita de {calcula_tinta(rendimento, altura, largura)} latas de tinta para pintar a parede.')

print('---')

#Desafio com 'Sets'

'''
Criar um programa que gera 3 listas de acordo com as informações abaixo:

Lista1= Funcionários que tem carro e trabalham à noite
Lista2= Funcionários que tem carro e trabalham de dia
Lista3= Funcionários que não tem carro

'''
funcionarios = ['Ana', 'João', 'Maria', 'José', 'Carlos', 'Mariana', 'Paulo', 'Pedro', 'Luana', 'Luiz']
turno_dia = ['Ana', 'João', 'Maria', 'José', 'Carlos']
turno_noite = ['Mariana', 'Paulo', 'Pedro', 'Luana', 'Luiz']
tem_carro = ['Ana', 'João', 'Maria', 'José', 'Carlos', 'Mariana', 'Paulo', 'Pedro']

# Lista1: Funcionários que têm carro e trabalham à noite
lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

# Lista2: Funcionários que têm carro e trabalham de dia
lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

# Lista3: Funcionários que não têm carro
lista3 = set(funcionarios).difference(tem_carro)
print(lista3)
# Fim do desafio com 'Sets'

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
# Fim do cálculo de IMC