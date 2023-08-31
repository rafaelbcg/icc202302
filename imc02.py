massa = float(input('massa: '))
altura = float(input('altura(m): '))

imc = massa /(altura)**2

if imc < 18.5:
    print('abaixo do peso - precisa comer um pouco mais.')
else:
    if 18.5 <= imc < 25:
        print('no peso. parabens')
    else:
        if 25 <= imc < 30:
            print('sobrepeso - precisa fazer uma dieta.')
        else:
            if 30 <= imc < 35:
                print('obesidade I - gordinho(a)')
            else:
                if 35 <= imc < 40:
                    print('obesidade II - gordo(a)')
                else:
                    if 40 <= imc < 45:
                        print('obesidade morbida - gordão')
                    else:
                        if 45 <= imc:
                            print('super-obesidade.')

print(f' oIMC eh de {imc}')
