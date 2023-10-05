import random

numeros = list()

for i in range(20):
    numeros.append(random.randint(20,200))


#maior = max(numeros)
maior = numeros[0]
for i in numeros:
    if i > maior:
        maior = i

#menor = min(numeros)
menor = numeros[0]
for i in numeros:
    if i < menor:
        menor = i

#soma = sum(numeros)
soma = 0
for i in numeros:
    soma += i

#media = soma/len(numeros)
tamanho = 0
for i in numeros:
    tamanho += 1

media = soma/tamanho

for i in numeros:
    print(i)

print(f'maior = {maior}')
print(f'menor = {menor}')
print(f'soma  = {soma}')
print(f'media = {media}')
