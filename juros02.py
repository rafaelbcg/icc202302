investimento = float(input('investimento: '))
juros = float(input('juros: '))

mes = 0
total = investimento
depositado = 0

while mes < 24:
    parcial = (juros*total)/100
    total += parcial + depositado
    mes += 1
    print(f'{mes:2d} mes - juros: {parcial:10.2f} reais')
    depositado = float(input('depositado: '))
    investimento += depositado

print(f'total pago: {total:12.2f} reais')
print(f'juros pago: {(total-investimento):12.2f} reais')
