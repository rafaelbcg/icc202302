temperatura = [-10,-8,0,1,2,5,-2,-4]

temperatura_ordenada = sorted(temperatura)

media = sum(temperatura)/len(temperatura)

print(f' maior temperatura: {temperatura_ordenada[::-1][0]} ºc')
print(f' menor temperatura: {temperatura_ordenada[0]} ºc')
print(f' media temperatura: {media} ºc')
