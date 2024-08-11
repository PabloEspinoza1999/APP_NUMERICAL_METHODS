from django.shortcuts import render
from django.http import HttpResponse
from ..Utils import USecante
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO


def ShowSecante(request):
    salario = 3000
    n_desarrolladores = 20
    horas_trabajo = 1000
    costo_total = n_desarrolladores * salario * (horas_trabajo / 160)
    print('Costo total', costo_total)


    # Función del ROI
    def ROI(p):
        ingresos = p * ventas(p)
        return (ingresos - costo_total) / costo_total



    p0, p1 = 500, 600
    precio_optimo, iteraciones = USecante.metodo_secante(ROI, p0, p1)

    print(f"El precio óptimo es: ${precio_optimo:.2f}", flush=True)
    print(f"El ROI en este punto es: {ROI(precio_optimo):.2f}", flush=True)
    print(f"La cantidad de ventas necesarias son: {ventas(precio_optimo):.2f}", flush=True)

    precios = np.linspace(0, 3000, 500)
    roi_values = ROI(precios)


    # Extraemos las iteraciones para graficar
    iter_precios, iter_rois = zip(*iteraciones)

    # Creamos la gráfica
    plt.figure(figsize=(12, 8))
    plt.plot(precios, roi_values, label='ROI vs Precio', color='blue')
    plt.axvline(x=precio_optimo, color='red', linestyle='--', label=f'Precio Óptimo: ${precio_optimo:.2f}')
    plt.scatter(precio_optimo, ROI(precio_optimo), color='red')

    # Graficamos las iteraciones
    plt.plot(iter_precios, iter_rois, 'o-', color='green', label='Iteraciones')

    # Añadimos etiquetas y título
    plt.title('Retorno de Inversión (ROI) en función del Precio con Iteraciones del Método de la Secante')
    plt.xlabel('Precio ($)')
    plt.ylabel('ROI')
    plt.legend()
    plt.grid(True)



    # Guardar la imagen en un objeto BytesIO
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    print("Generando imagen")

    response = HttpResponse(buf.getvalue(), content_type='image/png;base64')
    response['Content-Disposition'] = 'attachment; filename="grafica.png"'

    return response



def SaveSecante(request):
    if request.method == 'POST':
        try:
            x0 = float(request.POST.get('x0'))
            x1 = float(request.POST.get('x1'))
            tol = float(request.POST.get('tol'))
            max_iter = int(request.POST.get('max_iter'))

            # Definimos la función de desviación
            f = lambda T: 0.01 * T**2 - 0.5 * T + 3

            # Aplicamos el método de la secante
            resultado, num_iteraciones, iteraciones = USecante.AlgoritSecante(f, x0, x1, tol, max_iter)

            contexto = {
                'resultado': resultado,  # Esto es un float o None
                'iteraciones': iteraciones  # Esto es una lista de tuplas (iteración, valor)
            }
        except (ValueError, TypeError) as e:
            contexto = {
                'error_message': f"Error en los datos de entrada: {str(e)}"
            }

        return render(request, 'pages/ViewSecante/Index.html', contexto)

    return render(request, 'pages/ViewSecante/Index.html')


def ventas(p, V0=10000, alpha=0.01):
    return V0 * np.exp(-alpha * p)
