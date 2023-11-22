# rafael de brito

with open('texto.txt') as arquivo1:
    with open('novo_texto.txt') as arquivo2:
        with open('concatenado.txt', 'w') as arquivo3:
            linhas01 = arquivo1.readlines()
            linhas02 = arquivo2.readlines()
            linhas03 = linhas01 + linhas02
            for i in linhas03:
                arquivo3.write(i)
