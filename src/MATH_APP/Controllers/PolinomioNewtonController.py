import base64
from django.shortcuts import render
from django.http import HttpResponse
from ..Utils import UPolinomioNewton
from ..Data.Cliente_Polinomio import Cliente_PolinomioData

import numpy as np
from django.http import JsonResponse
Cliente_data = Cliente_PolinomioData()

def ShowPolinomioNewton(request):     
       lista_cliente = Cliente_data.get_all_clientes()
       return render(request, 'pages/ViewPolinomioNewton/Index.html',{'lista_cliente':lista_cliente})


def SavePolinomioNewton(request):
    try:
        # Datos de prueba por defecto
        t_points = [10.0, 15.0, 20.0]  # Ejemplo: precios como puntos de tiempo
        satisfaction_points = [4.5, 3.8, 4.2]  # Ejemplo: satisfacción del cliente como puntos

        # Validar los datos
        if len(t_points) == 0 or len(satisfaction_points) == 0 or len(t_points) != len(satisfaction_points):
            return JsonResponse({'error': 'Datos de entrada inválidos o incompletos.'}, status=400)

        # Generar la imagen con los datos proporcionados
        imagen, Ruta = UPolinomioNewton.get_plot_image(t_points, satisfaction_points)

        # Convertir la imagen en un formato que pueda ser mostrado en el template
        plot_image_data = 'data:image/png;base64,' + base64.b64encode(imagen).decode('utf-8')

        # Obtener datos de clientes
        lista_cliente = Cliente_data.get_all_clientes()

        # Contexto con la imagen en formato base64 y la lista de clientes
        contexto = {
            'lista_cliente': lista_cliente,
            'plot_image': plot_image_data,
            'Ruta': Ruta
        }

        # Renderizar el template con la imagen y la lista de clientes
        return render(request, 'pages/ViewPolinomioNewton/Index.html', contexto)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
