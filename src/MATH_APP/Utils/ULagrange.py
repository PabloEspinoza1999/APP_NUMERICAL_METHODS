import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

# Datos de satisfacción en diferentes puntos
t_points = np.array([1, 2, 3])
satisfaction_points = np.array([4.5, 4.0, 3.5])

# Función para calcular el polinomio de Lagrange
def lagrange_interpolation(t, t_points, satisfaction_points):
    n = len(t_points)
    L = 0
    for i in range(n):
        li = np.prod([(t - t_points[j]) / (t_points[i] - t_points[j]) for j in range(n) if j != i])
        L += satisfaction_points[i] * li
    return L


# Retornar el objeto BytesIO para la descarga
def get_plot_image():
    # Puntos para la gráfica
    t_values = np.linspace(1, 3, 100)
    satisfaction_values = [lagrange_interpolation(t, t_points, satisfaction_points) for t in t_values]

    # Graficar los puntos y el polinomio interpolante
    plt.figure(figsize=(10, 6))
    plt.plot(t_values, satisfaction_values, label='Interpolación de Lagrange')
    plt.scatter(t_points, satisfaction_points, color='red', zorder=5, label='Puntos de datos')
    plt.xlabel('Tiempo')
    plt.ylabel('Satisfacción')
    plt.title('Interpolación de Lagrange de la Satisfacción del Cliente')
    plt.legend()
    plt.grid(True)

    # Guardar la imagen en un objeto BytesIO
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    print("Generando imagen")

    return buf.getvalue()
