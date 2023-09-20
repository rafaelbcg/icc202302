import numpy as np

def volume(h, b1, b2, L):
    return 0.5 * h * (b1 + b2) * L

def muller_barragem(target_volume, h ,b1, b2, L, tol, max_iter):


    for i in range(max_iter):
        v0 = volume(h[0], b1, b2, L)
        v1 = volume(h[1], b1, b2, L)
        v2 = volume(h[2], b1, b2, L)

        f_h = v2 - target_volume

        if abs(f_h) < tol:
            return h2  # Altura da barragem encontrada

        a = (v1 - v0) / (h[1] - h[0])
        b = (v2 - v0) / (h[2] - h[0])
        c = (v2 - v1) / (h[2] - h[1])

        delta = b**2 - 4 * a * c

        if delta < 0:
            raise ValueError("Muller's method did not converge (complex roots)")

        denominator = b + np.sign(b) * np.sqrt(delta)

        if abs(denominator) < 1e-10:
            return h[2]  # Evitar divisão por zero

        h3 = h[2] - 2 * c / denominator

        # Atualização das estimativas
        h = [h[1],h[2],h3]

    raise ValueError("Muller's method did not converge")

# Dados do problema
target_volume = 100000  # Volume desejado em metros cúbicos
b1 = 50  # Base maior em metros
b2 = 10  # Base menor em metros
L = 200  # Comprimento em metros
tolerance = 0.001
max_iterations = 50
h = [25,35,40]

# Encontrar a altura da barragem
height_of_dam = muller_barragem(target_volume,h, b1, b2, L, tolerance, max_iterations)
print(f"A altura da barragem necessária é: {height_of_dam:.2f} metros")
