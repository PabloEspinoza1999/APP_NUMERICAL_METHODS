def AlgoritSecante(f, x0, x1, tol=1e-6, max_iter=100):
    iteraciones = []  # Lista para almacenar todas las iteraciones
    for i in range(max_iter):
        if abs(f(x1) - f(x0)) < tol:
            # Si la diferencia entre f(x1) y f(x0) es menor que la tolerancia, retornar el resultado actual
            return None, i, iteraciones
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))  # Cálculo del siguiente valor
        iteraciones.append((i + 1, x2))  # Añadir la iteración a la lista
        if abs(x2 - x1) < tol:
            # Si la diferencia entre x2 y x1 es menor que la tolerancia, retornar el resultado actual
            return x2, i + 1, iteraciones
        x0, x1 = x1, x2  # Actualizar x0 y x1 para la siguiente iteración
    # Si se alcanza el máximo número de iteraciones sin encontrar el resultado, retornar None
    return None, max_iter, iteraciones


def metodo_secante(f, p0, p1, tol=1e-5, max_iter=100):
    iteraciones = [(p0, f(p0))]
    for i in range(max_iter):
        f_p0 = f(p0)
        f_p1 = f(p1)
        if abs(f_p1 - f_p0) < tol:
            break
        p2 = p1 - f_p1 * (p1 - p0) / (f_p1 - f_p0)
        iteraciones.append((p2, f(p2)))
        if abs(p2 - p1) < tol:
            return p2, iteraciones
        p0, p1 = p1, p2
    return p1, iteraciones


