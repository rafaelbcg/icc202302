# rafael de brito


with open("texto.txt","r") as arquivo:
    linhas = arquivo.readlines()
    print(f'numero de linhas: {len(linhas)}')
    for i in linhas:
        print(i)

