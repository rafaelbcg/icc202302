num = int(input('fatorial: '))

fat = 1
i = 1

while i <= num:
    fat = fat * i
    i += 1

soma = 0
aux  =fat

while aux > 0:
    soma = soma + aux%10
    aux = aux//10

print(f'{num} != {fat} com soma = {soma}')
