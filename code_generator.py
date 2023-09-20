import random
import string

def gerar_codigo_unico(nome):
    letras = random.sample(string.ascii_letters, 2)
    numeros = random.sample(string.digits, 2)
    restante = random.sample(string.ascii_letters + string.digits, 4)
    codigo = ''.join(letras + numeros + restante)
    return codigo.upper()

personagens = ["Ana Oliveira", "Paula Costa", "Helena Garcia", "Mia Meyer", "Emma Muller"]

tabela = {}
for personagem in personagens:
    nome = personagem.split()[0].lower()  # Pegar o primeiro nome e torná-lo em letras minúsculas
    codigo = gerar_codigo_unico(nome)
    tabela[personagem] = codigo

print("{:<15} {:<8}".format("Personagem", "Código Único"))
for personagem, codigo in tabela.items():
    print("{:<15} {:<8}".format(personagem, codigo))
