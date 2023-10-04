import random

i = 0
faces = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

while i < 100000:
    sorteo = random.randint(1,20)
    faces[sorteo-1] += 1
    i += 1

print(f' foi feito {100000} lancamentos')
for j in range(len(faces)):
    print(f' a porcentagem da face {j+1} foi de {faces[j]/100000}')

        
    
