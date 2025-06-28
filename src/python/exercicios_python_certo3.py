# While Loop

# Dica: Atribuição aumentada +=, -=, *=, /=

x = 0
while x < 10:
    print(x)
    x = x + 1 # ou x += 1
    
print('---')

# Loop infinito e break

while True:
    resposta = input('Qual a capital do canadá? ')
    if resposta == 'Ottawa':
        print('Acertou!')
        break
    else:
        print('Tente novamente')
        
print('---')

# continue

while True:
    username = input('username? ')
    if username != 'neo':
        print('Nunca nem vi')
        continue
    senha = input('Qual a sua senha? ')
    if senha == '1234':
        print('Bem-vindo, {}'.format(username))
        print('Aceita um café? ')
        break
    
    print('---')
    
# Listas

planetas = ['Mercurio', 'Venus', 'Jupiter']
print(planetas[1])

print('---')

# for loops e range

for i in range(6) :
    print(i)

# or

for i in [0, 1, 2, 3, 4, 5] :
    print(i)
    
# range 

for x in range(1,15,2):
    print(x)

#
    
planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno']
for planeta in planetas:
        print(planeta)
planetas.append('Plutão') # chegai plutao :)

#

planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno', 'Plutão']
for p in planetas:
        print(p)
        
# 

for i in range(len(planetas)):
        print(i, planetas[i])
        
print('---')

# Enumerate
planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno', 'Plutão']
for i, planeta in enumerate(planetas):
    print(i, planeta)
    
    