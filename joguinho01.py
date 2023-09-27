palavra_secreta = 'HAMBURGUER'
dica = 'COMIDA DE FAST FOOD. PODE COMER NO PAO'

vezes = 1

while True:
    resposta = input('Sua resposta: ')
    if resposta.upper() == palavra_secreta:
        print('Acertou misarevel')
        print(f'precisou de {vezes} vezes para acertar.')
        break
    else:
        vezes +=1
        print(dica)

input()


