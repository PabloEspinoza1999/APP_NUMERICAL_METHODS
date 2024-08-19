from django.shortcuts import redirect, render
from ..Utils import UPolinomioNewton
from datetime import datetime
from ..Data.Cliente_Polinomio import Cliente_PolinomioData, Cliente_Polinomio
import numpy as np
from django.http import JsonResponse
from io import BytesIO
import pandas as pd

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
    


def import_clients(request):

    if request.method == 'POST':
        print('--------------------- Importando usuarios')
        print(request.FILES["listaclientes"], flush=True)
        
        file = request.FILES["listaclientes"]

        # Read the Excel file into a DataFrame
        df = pd.read_excel(BytesIO(file.read()))

        processed_data = []

        for index, row in df.iterrows():
            row_data = row.to_dict()
            cliente = Cliente_Polinomio(row_data['id'], row_data['cliente'], row_data['precio'], row_data['satisfaccion'])
            processed_data.append(cliente)

        Cliente_data.upate_clientes(processed_data)

        return JsonResponse({'message': '¡Datos han sido impotados!'}, status=200)

    else:
        return redirect('ShowPolinomioNewton')


def clean(request):
    Cliente_data.clean()
    return JsonResponse({'message': '¡Datos han sido limpiados!'}, status=200)

