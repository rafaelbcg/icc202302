massa = float(input('massa: '))
altura = float(input('altura(m): '))

imc = massa /(altura)**2

if imc < 18.5:
    print('abaixo do peso - precisa comer um pouco mais.')
if 18.5 <= imc < 25:
    print('no peso. parabens')
if 25 <= imc < 30:
    print('sobrepeso - precisa fazer uma dieta.')
if 30 <= imc < 35:
    print('obesidade I - gordinho(a)')
if 35 <= imc < 40:
    print('obesidade II - gordo(a)')
if 40 <= imc < 45:
    print('obesidade morbida - gordão')
if 45 <= imc:
    print('super-obesidade.')

print(f' oIMC eh de {imc}')
