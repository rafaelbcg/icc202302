with open('texto.txt','r') as arquivo:
    linhas = arquivo.readlines()

ordenados = sorted(linha)

with open('ordenado.txt','w') as ordenacao:
    for i in ordenados:
        ordenacao.write(i)
