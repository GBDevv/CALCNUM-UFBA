def secante(f, x0, x1, tol=1e-4, max_iter=20):
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)

        # Fórmula das Secantes
        x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0)

        # Critério de parada pelo erro relativo
        erro = abs(x2 - x1) / abs(x2)
        if erro < tol:
            return x2

        # Descarta o ponto mais antigo
        x0 = x1
        x1 = x2

    return x1


# Teste do slide: f(x) = x^2 - 2
f = lambda x: x**2 - 2
raiz = secante(f, x0=1.0, x1=2.0)

print("Raiz encontrada:", raiz)