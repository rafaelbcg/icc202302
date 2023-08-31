massa = float(input('massa: '))
altura = float(input('altura(m): '))

imc = massa /(altura)**2

if imc < 18.5:
    print('abaixo do peso - precisa comer um pouco mais.')
elif 18.5 <= imc < 25:
    print('no peso. parabens')
elif 25 <= imc < 30:
    print('sobrepeso - precisa fazer uma dieta.')
elif 30 <= imc < 35:
    print('obesidade I - gordinho(a)')
elif 35 <= imc < 40:
    print('obesidade II - gordo(a)')
elif 40 <= imc < 45:
    print('obesidade morbida - gordão')
elif 45 <= imc:
    print('super-obesidade.')

print(f' oIMC eh de {imc}')
