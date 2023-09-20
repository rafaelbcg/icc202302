import numpy as np

def f(x):
    return x**3 - 3*x**2 + 6*x - 9

def muller(f, x0, x1, x2, tol, max_iter):
    for i in range(max_iter):
        h1 = x1 - x0
        h2 = x2 - x1
        delta1 = (f(x1) - f(x0)) / h1
        delta2 = (f(x2) - f(x1)) / h2
        d = (delta2 - delta1) / (h2 + h1)

        b = delta2 + h2 * d
        D = np.sqrt(b**2 - 4*f(x2)*d)

        if abs(b - D) < abs(b + D):
            E = b + D
        else:
            E = b - D

        h = -2 * f(x2) / E
        p = x2 + h

        print(f"Iteração {i + 1}:")
        print(f"x0 = {x0:.4f}, x1 = {x1:.4f}, x2 = {x2:.4f}")
        print(f"f(x0) = {f(x0):.4f}, f(x1) = {f(x1):.4f}, f(x2) = {f(x2):.4f}")
        print(f"delta1 = {delta1:.4f}, delta2 = {delta2:.4f}, d = {d:.4f}")
        print(f"b = {b:.4f}, D = {D:.4f}, E = {E:.4f}")
        print(f"h = {h:.4f}, p = {p:.4f}")
        
        if abs(h) < tol:
            return p

        x0 = x1
        x1 = x2
        x2 = p

    raise ValueError("Muller's method did not converge")

x0 = 2.0
x1 = 2.5
x2 = 3.0
tolerance = 0.001
max_iterations = 20

root = muller(f, x0, x1, x2, tolerance, max_iterations)
print("\nA raiz encontrada é: {:.4f}".format(root))
