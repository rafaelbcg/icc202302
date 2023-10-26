def f(i):
    P = 35000
    A = 8500
    n = 7
    return A - P * (i * (1 + i)**n) / (((1 + i)**n) - 1)

x0 = 0.01
x1 = 0.3
epsilon = 0.05

while abs((x1 - x0) / x1) > epsilon*0.01:
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    print(f'{x0:.5f} - {f(x0):.5f}   {x1:.5f} - {f(x1):.5f}   {x2:.5f} - {f(x2):.5f}')
    x0, x1 = x1, x2

print("A taxa de juros é aproximadamente", x1)
