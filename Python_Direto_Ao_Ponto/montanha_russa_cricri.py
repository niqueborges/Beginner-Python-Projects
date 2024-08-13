#

'''idade = 17
altura = 1.4
ticket_valido = True
if ticket_valido:
    print('Seu ticket é válido')
elif idade > 18:
    print('Você é maior de idade')
elif altura > 1.5:
    print('Altura premitida')
else:
    print('Requisitos não atendidos')
'''

idade = 19
altura = 1.4
ticket_valido = True
if ticket_valido: 
    print('Seu ticket é válido')
elif idade > 18 and altura > 1.5:
    print('Entrada permitida')
else:
    print('Requisitos não atendidos')


