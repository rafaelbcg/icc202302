import math

def f(x):
    return math.log(x**2) - 0.7

a = 1
b = 2
epsilon = 0.00001

for i in range(5):
    c = (a*f(b) - b*f(a))/(f(b)-f(a))
    print(f'{a:.4f} - {f(a):.4f}   {b:.4f} - {f(b):.4f}   {c:.4f} - {f(c):.4f}')
    if abs(f(c)) < epsilon:
        break
    elif f(a) * f(c) < 0:
        b = c
    else:
        a = c

print("A raiz da função é aproximadamente", c)
