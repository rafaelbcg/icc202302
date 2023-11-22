def fibonacci(n:int) -> int:
    if n <=1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


lista = [10,20,30,40,50,60,70]

for i in lista:
    print(f' {i} {fibonacci(i)}')
