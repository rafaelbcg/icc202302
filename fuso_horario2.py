print('converte para horario de londres')
hora = int(input('hora em brasilia: '))
minuto = int(input('minuto em brasilia: '))

if hora+3 >= 24:
    print(f'em londres: {hora-21} horas e {minuto} minutos')
else:
    print(f'em londres: {hora+3} horas e {minuto} minutos')


#print('em londres: ',hora+3,' horas e ',minuto,' minutos')
