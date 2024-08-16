from ..Utils import UNewton
from datetime import datetime
import base64
from datetime import datetime
from django.shortcuts import redirect, render
from ..Data.Cliente_Newton import Cliente_NewtonData
Cliente_data = Cliente_NewtonData()

def Index(request):
    return render(request, 'pages/index.html')

def UserManual(request):
    return render(request, 'pages/UserManual/Index.html')

def ShowNewtonRaphson(request):
    try:
        lista_cliente = Cliente_data.get_all_clientes()
        if not lista_cliente:
            return render(request, 'pages/ViewNewtonRaphson/Index.html', {'error_message': 'No se encontraron datos de clientes.'})

        for cliente in lista_cliente:
            if isinstance(cliente.fecha_registro, datetime):
                cliente.fecha_registro = cliente.fecha_registro.strftime("%Y-%m-%d")
            cliente.tiempo_respuesta = round(cliente.tiempo_respuesta, 2)

        return render(request, 'pages/ViewNewtonRaphson/Index.html', {'lista_cliente': lista_cliente})

    except Exception as e:
        return render(request, 'pages/ViewNewtonRaphson/Index.html', {'error_message': str(e)})

def SaveNewtonRaphson(request):
    try:
        lista_cliente = Cliente_data.get_all_clientes()
        tiempos = [cliente.tiempo_respuesta for cliente in lista_cliente]
        if not tiempos:
            return render(request, 'pages/ViewNewtonRaphson/Index.html', {'error_message': 'Datos de entrada inválidos o incompletos.'})

        Tiempo, imagen, Ruta = UNewton.newton_raphson_optimize_cost(tiempos)
        plot_image_data = 'data:image/png;base64,' + imagen

        for cliente in lista_cliente:
            if isinstance(cliente.fecha_registro, datetime):
                cliente.fecha_registro = cliente.fecha_registro.strftime("%Y-%m-%d")
            cliente.tiempo_respuesta = round(cliente.tiempo_respuesta, 2)

        contexto = {
            'lista_cliente': lista_cliente,
            'plot_image': plot_image_data,
            'Ruta': Ruta,
            'Tiempo': Tiempo
        }

        return render(request, 'pages/ViewNewtonRaphson/Index.html', contexto)

    except Exception as e:
        return render(request, 'pages/ViewNewtonRaphson/Index.html', {'error_message': str(e)})
    


def SaveClient(request):
    if request.method == 'POST':
        try:
            cliente_data_dict = {
                'nombre_cliente': request.POST['nombre_cliente'],
                'tiempo_respuesta': float(request.POST['tiempo_respuesta']),
                'fecha_registro': request.POST['fecha_registro'],  
                'correo': request.POST['correo'],
                'telefono': request.POST['telefono'],
                'direccion': request.POST['direccion'],
                'tipo_cliente': request.POST['tipo_cliente'],
                'estado_cuenta': request.POST['estado_cuenta'],
                'preferencias': request.POST['preferencias'],
                'comentarios': request.POST.get('comentarios', '') 
            }

            Cliente_data.add_cliente(cliente_data_dict)
            return redirect('ShowNewtonRaphson')

        except Exception as e:
            return render(request, 'pages/ViewNewtonRaphson/Index.html', {'error_message': str(e)})

    else:
        lista_cliente = Cliente_data.get_all_clientes()
        for cliente in lista_cliente:
            if isinstance(cliente.fecha_registro, datetime):
                cliente.fecha_registro = cliente.fecha_registro.strftime("%Y-%m-%d")
            cliente.tiempo_respuesta = round(cliente.tiempo_respuesta, 2)

        return render(request, 'pages/ViewNewtonRaphson/Index.html', {'lista_cliente': lista_cliente})
    
def Deleteclient(request, id):
    if request.method == 'POST':
        try:
            Cliente_data.delete_cliente(id)
            return redirect('ShowNewtonRaphson') 
        except Exception as e:
            return render(request, 'pages/ViewNewtonRaphson/Index.html', {'error_message': str(e)})
    else:
        return redirect('ShowNewtonRaphson')  