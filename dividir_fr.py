def dividir_frase(frase :str):
    return frase.split(' ')


texto = input('>>> ')

partes = dividir_frase(texto)
for i in partes:
    print(i)

    
