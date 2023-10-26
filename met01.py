def ehPrimo(num:int) -> bool:
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

numeros = [23,26, 8, 71, 90,17]


for i in numeros:
    if ehPrimo(i):
        print(i)
