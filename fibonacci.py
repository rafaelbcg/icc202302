import time
penultimo = 1
ultimo = 1
print('programas que imprime a lista de n termos.')
termos = int(input("termos: "))
i = 0 #variavel de contagem - conta quantas vezes
while i < termos:
    if i <= 1:
        print(1)
    else:
        x = penultimo + ultimo
        print(x)
        time.sleep(1)
        penultimo, ultimo = ultimo, x
    i = i + 1

print('Acabou!!!')
