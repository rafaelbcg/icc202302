import random

num_secreto = random.randint(1,100)

num_chute = int(input('numero: '))

while num_chute != num_secreto:
    if num_chute > num_secreto:
        print('O numero secreto eh menor.')
    else:
        print('O numero secreto eh maior.')
    num_chute = int(input('numero: '))

print('Acertou! - numero sorteado foi: ',num_secreto)
