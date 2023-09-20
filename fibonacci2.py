import time
penultimo = 1
ultimo = 1
print('programas que imprime a lista de n termos menores que 1000.')

while ultimo < 1000:
    x = penultimo + ultimo
    print(ultimo)
    time.sleep(1)
    penultimo, ultimo = ultimo, x

print('Acabou!!!')
