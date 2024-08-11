import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

# Función para calcular los coeficientes del polinomio de Newton
def newton_coefficients(puntos_precios, satisfaction_points):
    n = len(puntos_precios)
    coeffs = np.copy(satisfaction_points)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coeffs[i] = (coeffs[i] - coeffs[i - 1]) / (puntos_precios[i] - puntos_precios[i - j])
    return coeffs


# Función para evaluar el polinomio de Newton
def newton_interpolation(t, puntos_precios, coeffs):
    n = len(puntos_precios)
    result = coeffs[-1]
    iterations = [(n - 1, result)]
    for i in range(n - 2, -1, -1):
        result = result * (t - puntos_precios[i]) + coeffs[i]
        iterations.append((i, result))
    return result, iterations


# Generar la imagen de la gráfica y devolverla junto con las iteraciones
def get_plot_image(puntos_precios, satisfaction_points):
    # Obtener los coeficientes del polinomio de Newton
    coeffs = newton_coefficients(puntos_precios, satisfaction_points)

    # Puntos para la gráfica
    t_values = np.linspace(min(puntos_precios), max(puntos_precios), 100)
    satisfaction_values = []
    all_iterations = []

    # Evaluar el polinomio y guardar las iteraciones
    for t in t_values:
        satisfaction, iterations = newton_interpolation(t, puntos_precios, coeffs)
        satisfaction_values.append(satisfaction)
        all_iterations.append(iterations)

    # Graficar los puntos y el polinomio interpolante
    plt.figure(figsize=(12, 6))
    plt.plot(t_values, satisfaction_values, label='Pronóstico')
    plt.scatter(puntos_precios, satisfaction_points, color='red', zorder=5, label='Satisfacción')
    plt.xlabel('Precio')
    plt.ylabel('Satisfacción')
    plt.title('Interpolación de Newton de la Satisfacción del Cliente')
    plt.legend()
    plt.grid(True)

    # Guardar la imagen en un objeto BytesIO
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    # Preparar las iteraciones para ser devueltas
    iteraciones_resultado = [
        {"iteracion": iteracion, "valor": valor}
        for iters in all_iterations for iteracion, valor in iters
    ]

    return buf.getvalue(), iteraciones_resultado