def fibonacci(n:int) -> int:
    x0 = 0
    x1 = 1
    i = 0
    while i < n:
        x0,x1 = x1,x1+x0
        i += 1
    return x1


lista = [10,20,30,40,50,60,70]

for i in lista:
    print(f' {i} {fibonacci(i)}')
