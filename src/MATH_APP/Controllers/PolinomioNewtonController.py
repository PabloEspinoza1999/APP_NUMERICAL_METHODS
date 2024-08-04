from django.shortcuts import render
from django.http import HttpResponse
from ..Utils import UPolinomioNewton
import numpy as np
from django.http import JsonResponse

def ShowPolinomioNewton(request):
    return render(request, 'pages/ViewPolinomioNewton/Index.html')
def SavePolinomioNewton(request):
    try:
        # Extraer datos de la solicitud y convertirlos en listas de flotantes
        t_points = list(map(float, request.GET.get('t_points', '').split(',')))
        satisfaction_points = list(map(float, request.GET.get('satisfaction_points', '').split(',')))

        # Validar los datos
        if len(t_points) == 0 or len(satisfaction_points) == 0 or len(t_points) != len(satisfaction_points):
            return JsonResponse({'error': 'Datos de entrada inválidos o incompletos.'}, status=400)

        # Generar la imagen con los datos proporcionados
        image_data = UPolinomioNewton.get_plot_image(t_points, satisfaction_points)
        return HttpResponse(image_data, content_type='image/png')
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)