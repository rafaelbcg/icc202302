import random

i = 0
face1 = 0
face2 = 0
face3 = 0
face4 = 0
face5 = 0
face6 = 0

while i < 100000:
    sorteo = random.randint(1,6)
    if sorteo == 1:
        face1 += 1
    elif sorteo == 2:
        face2 += 1
    elif sorteo == 3:
        face3 += 1
    elif sorteo == 4:
        face4 += 1
    elif sorteo == 5:
        face5 += 1
    else:
        face6 += 1
    i += 1

print(f' foi feito {100000} lancamentos')
print(f' a porcentagem da face 1 foi de {face1/100000}')
print(f' a porcentagem da face 2 foi de {face2/100000}')
print(f' a porcentagem da face 3 foi de {face3/100000}')
print(f' a porcentagem da face 4 foi de {face4/100000}')
print(f' a porcentagem da face 5 foi de {face5/100000}')
print(f' a porcentagem da face 6 foi de {face6/100000}')

        
    
