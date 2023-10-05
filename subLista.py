l1 = [11,10,9,14,15,7,8,14,20]

num = int(input('numero para procurar: '))

if num in l1:
    print(f'O número {num} está na posição {l1.index(num)}')
else:
    print('nao existe')
l2 = []
l3 = []
l4 = []

for i in l1:
    if i%2 == 0:
        l2.append(i)
    else:
        l3.append(i)

for i in l1:
    if not i in l4:
        l4.append(i)

print(l2)
print(l3)
print(l4)
