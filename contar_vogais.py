def contarVogais(palavra :str) -> int:
    contar = 0
    vogais = 'AEIOU'
    for i in vogais:
        contar += palavra.upper().count(i)

    return contar


print(contarVogais('Rafael'))
print(contarVogais('Quimica'))
print(contarVogais('Gabriela'))
