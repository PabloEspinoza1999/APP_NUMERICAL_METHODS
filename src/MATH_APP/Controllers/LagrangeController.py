from django.shortcuts import render
from django.http import HttpResponse
from ..Utils import ULagrange

def Index(request):
    return render(request, 'pages/ViewLagrange/Index.html')


def DownloadChart(request):
    response = HttpResponse(ULagrange.get_plot_image(), content_type='image/png;base64')
    response['Content-Disposition'] = 'attachment; filename="grafica.png"'

    return response
