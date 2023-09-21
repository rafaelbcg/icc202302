divida = float(input('divida: '))
juros = float(input('juros: '))

mes = 0
total = divida

while mes < 24:
    parcial = (juros*total)/100
    total += parcial
    mes += 1
    print(f'{mes:2d} mes - juros: {parcial:10.2f} reais')

print(f'total pago: {total:12.2f} reais')
print(f'juros pago: {(total-divida):12.2f} reais')
