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

# Fim