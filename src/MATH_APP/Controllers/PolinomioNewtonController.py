import base64
from django.shortcuts import render
from ..Utils import UPolinomioNewton
from ..Data.Cliente_Polinomio import Cliente_PolinomioData

import numpy as np
from django.http import JsonResponse
Cliente_data = Cliente_PolinomioData()

def ShowPolinomioNewton(request):
    lista_cliente = Cliente_data.get_all_clientes()

    for cliente in lista_cliente:
        cliente.precio = round(cliente.precio, 2)
        cliente.satisfaccion_cliente = round(cliente.satisfaccion_cliente, 2)
    return render(request, 'pages/ViewPolinomioNewton/Index.html', {'lista_cliente': lista_cliente })


def SavePolinomioNewton(request):
    try:
        # Se obtienen nos respectivos puntos
        puntos_precios      = [cliente.precio for cliente in Cliente_data.clientes]
        puntos_satisfaccion = [cliente.satisfaccion_cliente for cliente in Cliente_data.clientes]

        # Validar los datos
        if len(puntos_precios) == 0 or len(puntos_satisfaccion) == 0 or len(puntos_precios) != len(puntos_satisfaccion):
            return JsonResponse({'error': 'Datos de entrada inválidos o incompletos.'}, status=400)

        # Generar la imagen con los datos proporcionados
        imagen, Ruta = UPolinomioNewton.get_plot_image(puntos_precios, puntos_satisfaccion)

        # Convertir la imagen en un formato que pueda ser mostrado en el template
        plot_image_data = 'data:image/png;base64,' + base64.b64encode(imagen).decode('utf-8')

        # Obtener datos de clientes
        lista_cliente = Cliente_data.get_all_clientes()
        for cliente in lista_cliente:
            cliente.precio = round(cliente.precio, 2)
            cliente.satisfaccion_cliente = round(cliente.satisfaccion_cliente, 2)

        # Contexto con la imagen en formato base64 y la lista de clientes
        contexto = {
            'lista_cliente': lista_cliente,
            'plot_image': plot_image_data,
            'Ruta': Ruta
        }

        # Renderizar el template con la imagen y la lista de clientes
        return render(request, 'pages/ViewPolinomioNewton/Index.html', contexto)
    
    except Exception as e:
        return JsonResponse({'error': e}, status=500)
