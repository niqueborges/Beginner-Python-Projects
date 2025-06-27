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


