import random

alunos = ['DANILO', 'THALINE', 'LUCIMAR', 'PEDRO', 'SAMUEL', 'GABRIELA', 'ARIELLY', 'ADALBERTO']

continuar = 'SIM'

while continuar.upper() == 'SIM':
    palavra = random.choice(alunos)

    aux = ''
    for i in palavra:
        aux = aux + '_'

    vida = 3
    while vida > 0 and aux != palavra:
        print(aux)
        letra = input('digite a letra: ')
        while len(letra) > 1:
            print('mais de uma letra.')
            letra = input('digite a letra: ')
        if letra.upper() in palavra:
            aux1 = ''
            for j in range(len(palavra)):
                if letra.upper() != palavra[j] and aux[j] == '_':
                    aux1 = aux1 + '_'
                else:
                    
                    aux1 = aux1 + f'{palavra[j]}'
            aux,aux1 = aux1,''
        else:
            vida -= 1
        print(aux)
        print('sua vida: ',vida)
    if vida > 0:
        print('parabens, acertou')
    else:
        print('perdeu')
    print(palavra)
    print('Deseja continuar, digite SIM')
    continuar = input('>>> ')
    
