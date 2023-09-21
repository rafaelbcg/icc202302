import math

numero = float(input('numero: '))

raiz1 = numero **(1/2)
raiz2 = math.sqrt(numero)

# p = (b+(n/b))/2

parcial = 2
auxiliar = 2

while abs(parcial**2 - numero) > 0.0001:
    print(parcial**2)  
    parcial = (auxiliar + (numero/auxiliar))/2
    auxiliar = parcial

print("raiz quadrada de ",numero," eh igual a:")
print("por ^(1/2): ",raiz1)
print("por math.sqrt(n): ",raiz2)
print("por newton: ",parcial)




