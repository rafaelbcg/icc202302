'''
Resolução das questões 5, 6 

'''

with open('texto.txt', 'r') as arquivo:
    texto = arquivo.read() #ler todo o arquivo como uma unica string
    texto = texto.replace('velho', 'novo') #troca um sub grupo de strfing por outra
    print(f' vezes que aparecer palavra Python: {texto.count("Python")}')

with open('texto.txt','w') as arquivo: #'w' permite sobrescrever o arquivo
    arquivo.write(texto)
