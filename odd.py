def number_odd(l : list):
    elements = set(l)
    hapen = list()
    for i in elements:
        occurs = l.count(i)
        t = (i,occurs)
        hapen.append(t)

    return max(hapen,key=lambda x: x[1]%2!=0)

sample=[[7],[0],[1,1,2],[0,1,0,1,0]]

for i in sample:
    aux = number_odd(i)
    print(f' return {aux[0]} because occurs {aux[1]} times')
