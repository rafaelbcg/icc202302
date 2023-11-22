def paraDEC(txt : str):
    txt_dec = ''
    for i in txt:
        numDec = str(ord(i))
        txt_dec = txt_dec + numDec + ' '
    return txt_dec


print('transforma texto em codigo ascii')

texto = input('>> ')

print(paraDEC(texto))
