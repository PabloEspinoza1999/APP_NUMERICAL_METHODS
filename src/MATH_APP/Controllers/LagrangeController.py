from django.shortcuts import render
from django.http import HttpResponse
from ..Utils import ULagrange
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def Index(request):
    contexto = {
        'valor_x':  None,
        'valor_y':  None,
        'costo_minimo':  None
    }

    return render(request, 'pages/ViewLagrange/Index.html', context=contexto)



def calculate(request):
    if request.method == 'POST':
        presupuesto = float(request.POST.get('presupuesto'))
        costo       = float(request.POST.get('costo'))
        costo_base  = float(request.POST.get('costo_base'))
        # Función de callback para registrar iteraciones
        iteraciones = []

        # Definimos la función objetivo (maximizar x)
        def objective_function(vars):
            x, y = vars
            return -x  # Maximizar x es equivalente a minimizar -x


        # Definimos la restricción
        def constraint(vars):
            x, y = vars
            return presupuesto - (costo * x + y)


        def callback_function(vars):
            iteraciones.append(vars)

        def generate_lagrange_function():
            # Definir las variables de la función Lagrange
            x = 'x'
            y = 'y'
            lambd = 'λ'

            # Definir la función objetivo y la restricción
            objective_function = f"-{x}"
            constraint = f"{presupuesto} - ({costo}*{x} + {y})"

            # Combinar en la función de Lagrange
            lagrange_function = f"𝓛({x}, {y}, {lambd}) = {objective_function} + {lambd} * ({constraint})"
            
            return lagrange_function
        


        # Inicializamos el punto de partida
        initial_guess = [0, 0]  # Comenzamos en x=0, y=0

        # Definimos la restricción en el formato que acepta 'minimize'
        con = {'type': 'ineq', 'fun': constraint}

        # Usar el optimizador para maximizar la función (es decir, minimizar -x)
        result = minimize(objective_function, initial_guess, constraints=con, bounds=((0, None), (0, None)), callback=callback_function)

        contexto = {}

        # Imprimir los resultados
        if result.success:
            optimized_x, optimized_y = result.x
            costo_total = costo * optimized_x + optimized_y + costo_base

            ########################################################## Se procede a generar la gráfica
            # Definir el rango de x (número de productos)
            x_vals = np.linspace(0, 60, 100)  # Rango de productos fabricados

            # Calcular y basado en la restricción
            y_vals = presupuesto - costo * x_vals  # Restricción: y = 10000 - 200x

            # Crear la gráfica
            plt.figure(figsize=(10, 6))

            # Graficar la restricción de presupuesto
            plt.plot(x_vals, y_vals, label=f'Restricción ({costo:.0f}x + y = {presupuesto:.0f})', linestyle='--', color='r')

            # Calcular la evolución del precio total en cada iteración
            prices = [costo * iteration[0] + iteration[1] for iteration in iteraciones]

            # Graficar la evolución del precio total en cada iteración
            iterations_count = list(range(1, len(prices) + 1))
            plt.plot(iterations_count, prices, marker='o', linestyle='-', color='b', label='Evolución del Precio Total')

            # Marcar el punto óptimo
            optimal_price = costo * optimized_x + optimized_y
            plt.scatter(len(iteraciones), optimal_price, color='green', s=100, label=f'Punto Máximo: Productos=${optimized_x:.2f}', zorder=5)

            # Configurar la gráfica
            plt.title('Evolución del Precio Total y Restricción de Presupuesto')
            plt.xlabel('Número de Iteración')
            plt.ylabel('Precio Total ($)')
            plt.legend()
            plt.grid(True)


            #Guardar la imagen en un objeto BytesIO
            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            plt.close()
            imagen = 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode('utf-8')

            print(f"El valor óptimo de x (número de productos fabricados) es: {optimized_x:.0f}", flush=True)
            print(f"El costo adicional y óptimo es: {optimized_y:.2f}", flush=True)
            print(f"El costo mínimo total es: {costo_total:.2f}", flush=True)


            contexto = {
                'valor_x'     : optimized_x, # cantidad de productos que se pueden fabricar
                'valor_y'     : optimized_y, # costo base mínimo
                'costo_total' : costo_total, # costo total mínimo,
                'presupuesto' : presupuesto,
                'costo'       : costo,
                'costo_base'  : costo_base,
                'iteraciones' : iteraciones,
                'imagen'      : imagen,
                'funcion_lagrange' : generate_lagrange_function(),
                #'restriccion' : restriccion
            }
        else:
            print("No se pudo encontrar una solución óptima.", flush=True)

        return render(request, 'pages/ViewLagrange/Index.html', context=contexto)




def DownloadChart(request):
    response = HttpResponse(ULagrange.get_plot_image(), content_type='image/png;base64')
    response['Content-Disposition'] = 'attachment; filename="grafica.png"'

    return response
