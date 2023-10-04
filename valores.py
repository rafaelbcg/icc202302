import random

numeros = list()

for i in range(20):
    numeros.append(random.randint(20,200))


maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
media = soma/len(numeros)

for i in numeros:
    print(i)

print(f'maior = {maior}')
print(f'menor = {menor}')
print(f'soma  = {soma}')
print(f'media = {media}')
