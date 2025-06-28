age = int(input('Digite a sua idade: '))

if age < 13:
    print('Voce é uma crianca!')
elif age >= 13 and age < 20:
    print('Voce é um adolescente!')
else:
    print('Voce é um adulto!')