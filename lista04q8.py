'''
solução das questões 8, 9, 10
'''

linhas = []
tamanho = 0
tem_palavra = False
with open('texto.txt','r') as arquivo:
        aux = arquivo.readlines()
        for i in aux:
            #solucao da questão 10
            if i.count('programação') > 0:
                tem_palavra = True

            #solucao da questão 9
            tamanho += len(i)

            #solucao da questão 8
            if i != '' and i != "":
                linhas.append(i)

#solucao da questão 9        
media = tamanho / len(aux)

print(f'tamanho medio das string eh {media}')

#solucao da questão 10
if tem_palavra:
    print('Contém a palavra programação')

with open('sem_linhas_vazias.txt','w') as ordenacao:
    for i in linhas:
        ordenacao.write(i)
