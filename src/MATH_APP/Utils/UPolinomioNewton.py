import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Función para calcular los coeficientes del polinomio de Newton
def newton_coefficients(t_points, satisfaction_points):
    n = len(t_points)
    coeffs = np.copy(satisfaction_points)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coeffs[i] = (coeffs[i] - coeffs[i - 1]) / (t_points[i] - t_points[i - j])
    return coeffs

# Función para evaluar el polinomio de Newton
def newton_interpolation(t, t_points, coeffs):
    n = len(t_points)
    result = coeffs[-1]
    for i in range(n - 2, -1, -1):
        result = result * (t - t_points[i]) + coeffs[i]
    return result

# Generar la imagen de la gráfica y devolverla como respuesta HTTP
def get_plot_image(t_points, satisfaction_points):
    # Obtener los coeficientes del polinomio de Newton
    coeffs = newton_coefficients(t_points, satisfaction_points)

    # Puntos para la gráfica
    t_values = np.linspace(min(t_points), max(t_points), 100)
    satisfaction_values = [newton_interpolation(t, t_points, coeffs) for t in t_values]

    # Graficar los puntos y el polinomio interpolante
    plt.figure(figsize=(10, 6))
    plt.plot(t_values, satisfaction_values, label='Interpolación de Newton')
    plt.scatter(t_points, satisfaction_points, color='red', zorder=5, label='Puntos de datos')
    plt.xlabel('Tiempo')
    plt.ylabel('Satisfacción')
    plt.title('Interpolación de Newton de la Satisfacción del Cliente')
    plt.legend()
    plt.grid(True)

    # Guardar la imagen en un objeto BytesIO
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf.getvalue()