from django.shortcuts import render
from ..Utils import UNewton  # Asegúrate de que el import sea correcto
from django.http import JsonResponse

def Index(request):
    return render(request, 'pages/index.html')

def ShowNewtonRaphson(request):
    return render(request, 'pages/ViewNewtonRaphson/index.html')

def SaveNewtonRaphson(request):
    if request.method == 'POST':
        precio = float(request.POST.get('precio'))
        costo = float(request.POST.get('costo'))
        cantidad_maxima_demandada = float(request.POST.get('cantidad_maxima_demandada'))
        tasa_cambio_demanda_precio = float(request.POST.get('tasa_cambio_demanda_precio'))    
        try:
            ruta_punto_optimo = UNewton.newton_raphson_precio(precio, costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio)         
            ultimo_valor = ruta_punto_optimo[-1]
            contexto = {
                  'ruta_punto_optimo': ruta_punto_optimo,
                  'ultimo_valor': ultimo_valor
                  }
            return render(request, 'pages/ViewNewtonRaphson/index.html', contexto)
        except Exception as e:
            error_message = "Error: {}".format(str(e))
            return render(request,'pages/ViewNewtonRaphson/index.html', {'error_message': error_message})
    else:
        return render(request, 'pages/index.html')