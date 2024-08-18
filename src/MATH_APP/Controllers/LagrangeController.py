from django.shortcuts import render
from django.http import HttpResponse
from ..Utils import ULagrange
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from io import BytesIO
import base64


def Index(request):
    contexto = {
        'valor_x':  None,
        'valor_y':  None,
        'costo_minimo':  None
    }

    return render(request, 'pages/ViewLagrange/Index.html', context=contexto)



def calculate_cost(request):

    presupuesto = 10000
    costo = 200
    costo_base = 3

    # Definimos la función objetivo (maximizar x)
    def objective_function(vars):
        x, y = vars
        return -x  # Maximizar x es equivalente a minimizar -x


    # Definimos la restricción
    def constraint(vars):
        x, y = vars
        return presupuesto - (costo * x + y)

    # Función de callback para registrar iteraciones
    iteraciones = []

    def callback_function(vars):
        iteraciones.append(vars)

    # Inicializamos el punto de partida
    initial_guess = [0, 0]  # Comenzamos en x=0, y=0

    # Definimos la restricción en el formato que acepta 'minimize'
    con = {'type': 'ineq', 'fun': constraint}

    # Usar el optimizador para maximizar la función (es decir, minimizar -x)
    result = minimize(objective_function, initial_guess, constraints=con, bounds=((0, None), (0, None)), callback=callback_function)


    # Se procede a generar la gráfica
    # Extraer los valores de x a lo largo de las iteraciones
    x_values = [iteration[0] for iteration in iteraciones]

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, marker='o', linestyle='-', color='b')
    plt.title('Evolución del Número de Productos Fabricados (x) en Cada Iteración')
    plt.xlabel('Número de Iteración')
    plt.ylabel('Número de Productos Fabricados (x)')
    plt.grid(True)

    #Guardar la imagen en un objeto BytesIO
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    imagen = 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode('utf-8')

    contexto = {}

    # Imprimir los resultados
    if result.success:
        optimized_x, optimized_y = result.x
        costo_total = costo * optimized_x + optimized_y + costo_base

        print(f"El valor óptimo de x (número de productos fabricados) es: {optimized_x:.0f}", flush=True)
        print(f"El costo adicional y óptimo es: {optimized_y:.2f}", flush=True)
        print(f"El costo mínimo total es: {costo_total:.2f}", flush=True)


        contexto = {
            'valor_x'     :  optimized_x, # cantidad de productos que se pueden fabricar
            'valor_y'     :  optimized_y, # costo base mínimo
            'costo_total' :  costo_total, # costo total mínimo,
            'presupuesto' : presupuesto,
            'costo_base'  : costo_base,
            'iteraciones' : iteraciones,
            'imagen'      : imagen
        }
    else:
        print("No se pudo encontrar una solución óptima.", flush=True)

    return render(request, 'pages/ViewLagrange/Index.html', context=contexto)




def DownloadChart(request):
    response = HttpResponse(ULagrange.get_plot_image(), content_type='image/png;base64')
    response['Content-Disposition'] = 'attachment; filename="grafica.png"'

    return response
