def secant_method(f, x0, x1, tol=1e-5, max_iter=100):
    iteraciones = []  # Para almacenar el valor de cada iteración
    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
                
        # Almacenar las iteraciones actuales
        iteraciones.append((i, x0, x1))
                    
        # Fórmula de la secante para encontrar la siguiente aproximación
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
                
        # Verificar si la convergencia ha sido alcanzada
        if abs(x2 - x1) < tol:
            iteraciones.append((i + 1, x1, x2))
            return x2, iteraciones
                    
        # Actualizar los puntos
        x0, x1 = x1, x2
            
    raise ValueError("El método de la secante no ha convergido")

