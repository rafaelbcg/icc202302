def muller_method(f, x0, x1, x2, tol, max_iter):
    """
    Encontra uma aproximação da raiz da função f(x) usando o método de Muller.
    
    :param f: A função para a qual queremos encontrar a raiz.
    :param x0, x1, x2: Três pontos iniciais distintos para o método.
    :param tol: Tolerância, critério de parada (a diferença entre as iterações consecutivas).
    :param max_iter: Número máximo de iterações.
    
    :return: Aproximação da raiz da função f(x).
    """
    h0 = x1 - x0
    h1 = x2 - x1
    delta0 = (f(x1) - f(x0)) / h0
    delta1 = (f(x2) - f(x1)) / h1
    a = (delta1 - delta0) / (h1 + h0)
    
    i = 2
    while i <= max_iter:
        b = delta1 + h1 * a
        c = f(x2)
        discriminant = (b**2 - 4 * a * c)**0.5  # Raiz quadrada do discriminante
        
        # Escolha a raiz com o sinal correto para a convergência
        if abs(b + discriminant) > abs(b - discriminant):
            den = b + discriminant
        else:
            den = b - discriminant
        
        dx = -2 * c / den
        x = x2 + dx
        
        if abs(dx) < tol:
            return x
        
        x0, x1, x2 = x1, x2, x  # Atualiza os pontos para a próxima iteração
        h0 = x1 - x0
        h1 = x2 - x1
        delta0 = (f(x1) - f(x0)) / h0
        delta1 = (f(x2) - f(x1)) / h1
        a = (delta1 - delta0) / (h1 + h0)
        i += 1
    
    raise Exception("O método de Muller atingiu o número máximo de iterações.")

# Exemplo de uso:
def funcao_exemplo(x):
    return x**3 - 3*x**2 + 6*x - 9

x0 = 2.0
x1 = 2.5
x2 = 3.0
tolerancia = 0.0001
max_iteracoes = 100

raiz_aproximada = muller_method(funcao_exemplo, x0, x1, x2, tolerancia, max_iteracoes)
print(f"Aproximação da raiz: {raiz_aproximada:.6f}")
