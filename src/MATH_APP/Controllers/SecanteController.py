from django.shortcuts import render
from ..Utils import USecante  # Asegúrate de que el import sea correcto
from django.http import JsonResponse

def ShowSecante(request):
    return render(request, 'pages/ViewSecante/Index.html')

def SaveSecante(request):
    if request.method == 'POST':
        try:
            x0 = float(request.POST.get('x0'))
            x1 = float(request.POST.get('x1'))
            tol = float(request.POST.get('tol'))
            max_iter = int(request.POST.get('max_iter'))

            # Definimos la función de desviación
            f = lambda T: 0.01 * T**2 - 0.5 * T + 3

            resultado, num_iteraciones, iteraciones = USecante.AlgoritSecante(f, x0, x1, tol, max_iter)

            contexto = {
                'resultado': resultado,  
                'iteraciones': iteraciones  
            }
        except (ValueError, TypeError) as e:
            contexto = {
                'error_message': f"Error en los datos de entrada: {str(e)}"
            }

        return render(request, 'pages/ViewSecante/Index.html', contexto)

    return render(request, 'pages/ViewSecante/Index.html')
