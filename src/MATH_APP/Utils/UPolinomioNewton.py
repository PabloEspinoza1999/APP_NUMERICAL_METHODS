import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def diferencias_divididas(x, y):
    n = len(x)
    tabla = np.zeros((n, n))
    tabla[:, 0] = y

    operaciones = []

    for j in range(1, n):
        operaciones.append(f"\nCalculando diferencias divididas para j = {j}:")
        for i in range(n - j):
            numerador = tabla[i + 1, j - 1] - tabla[i, j - 1]
            denominador = x[i + j] - x[i]
            tabla[i, j] = numerador / denominador
            
            # Almacenar cada operación
            operaciones.append(f"tabla[{i}, {j}] = ({tabla[i + 1, j - 1]} - {tabla[i, j - 1]}) / ({x[i + j]} - {x[i]})")
            operaciones.append(f"tabla[{i}, {j}] = {numerador} / {denominador}")
            operaciones.append(f"tabla[{i}, {j}] = {tabla[i, j]:.4f}")

    return tabla, operaciones

def evaluar_polinomio(tabla, x_dato, x):
    n = len(x)
    resultado = tabla[0, 0]
    producto = 1

    for j in range(1, n):
        producto *= (x_dato - x[j - 1])
        resultado += tabla[0, j] * producto

    return resultado

def generar_imagen_grafico(x, tabla):
    # Ampliar el rango de evaluación para incluir más puntos
    precios_dato = np.linspace(min(x) - 50, max(x) + 50, 1000)
    satisfacciones = [evaluar_polinomio(tabla, precio, x) for precio in precios_dato]

    # Crear la figura del gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(precios_dato, satisfacciones, label='Polinomio Interpolador')
    plt.scatter(x, [evaluar_polinomio(tabla, xi, x) for xi in x], color='red', zorder=5, label='Puntos de Datos')
    plt.xlabel('Precio')
    plt.ylabel('Satisfacción')
    plt.title('Gráfico del Polinomio Interpolador')
    plt.legend()
    plt.grid(True)

    # Guardar la imagen en un buffer y convertirla a base64
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    plot_image_data = base64.b64encode(buf.getvalue()).decode('utf-8')
    return plot_image_data

def encontrar_precio_optimo(x, y):
    tabla, operaciones = diferencias_divididas(x, y)
    precios_dato = np.linspace(min(x) - 50, max(x) + 50, 1000)
    satisfacciones = [evaluar_polinomio(tabla, precio, x) for precio in precios_dato]

    precio_optimo = precios_dato[np.argmax(satisfacciones)]

    return tabla, operaciones, precio_optimo, max(satisfacciones)
