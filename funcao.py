import time

def funcao(x:float)->float:
    return x/(1-x)

def erro_absoluto(ybarra:float,y:float)->float:
    return abs(ybarra-y)

def erro_relativoPor(ybarra:float,y:float)->float:
    return (erro_absoluto(ybarra,y)/y)*100

termo = 0
x = 0.01

for i in range(20):
    termo = termo + x**i    
    ea = erro_absoluto(funcao(x),termo)
    er = erro_relativoPor(funcao(x),termo)
    print(f"{i+1} {termo} EA={ea} ER%={er}")
    time.sleep(1)

print(funcao(x))
input('>>>')

    
