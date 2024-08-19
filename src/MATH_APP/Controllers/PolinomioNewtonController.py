import base64
from django.shortcuts import render
from ..Utils import UPolinomioNewton
from ..Data.Cliente_Polinomio import Cliente_PolinomioData
import numpy as np
from django.http import JsonResponse
Cliente_data = Cliente_PolinomioData()

def ShowPolinomioNewton(request):
    try:
        lista_cliente = Cliente_data.get_all_clientes()
        for cliente in lista_cliente:
            cliente.precio = round(cliente.precio, 2)
            cliente.satisfaccion_cliente = round(cliente.satisfaccion_cliente, 2)
        
        contexto = {
            'lista_cliente': lista_cliente,
            'tabla': [] ,
            'headers': [] 
        }
        return render(request, 'pages/ViewPolinomioNewton/Index.html', contexto)

    except Exception as e:
        # Manejo de errores
        return JsonResponse({'error': str(e)}, status=500)

def SavePolinomioNewton(request):
    try:
        lista_cliente = Cliente_data.get_all_clientes()
        x = [cliente.precio for cliente in lista_cliente]
        y = [cliente.satisfaccion_cliente for cliente in lista_cliente]
       
        tabla, operaciones, precio_optimo, max_satisfaccion = UPolinomioNewton.encontrar_precio_optimo(x, y)
        
        if isinstance(tabla, np.ndarray):
            tabla = tabla.tolist()
        
        imagen_grafico = UPolinomioNewton.generar_imagen_grafico(x, np.array(tabla))
        
        contexto = {
            'tabla': tabla,
            'lista_cliente': lista_cliente,
            'operaciones': operaciones,
            'precio_optimo': precio_optimo,
            'max_satisfaccion': max_satisfaccion,
            'imagen_grafico': imagen_grafico
        }
        return render(request, 'pages/ViewPolinomioNewton/Index.html', contexto)

    except Exception as e:
        contexto = {
            'error_message': str(e),
            'lista_cliente': Cliente_data.get_all_clientes(), 
        }
        return render(request, 'pages/ViewPolinomioNewton/Index.html', contexto)