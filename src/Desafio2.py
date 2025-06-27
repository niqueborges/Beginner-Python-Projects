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
