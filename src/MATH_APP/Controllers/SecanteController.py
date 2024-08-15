from django.shortcuts import render
from django.http import HttpResponse
from ..Utils import USecante
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO


def ShowSecante(request):
    context = {'resultado' : None, 'iteraciones': None }
    return render(request, 'pages/ViewSecante/Index.html', context=context)



def SaveSecante(request):
    if request.method == 'POST':
        try:
            salario           = float(request.POST.get('salario_mensual'))
            n_desarrolladores = float(request.POST.get('total_personal'))
            horas_trabajo     = float(request.POST.get('horas_trabajo'))
            costo_total       = n_desarrolladores * salario * (horas_trabajo / 160)

            # Función del ROI
            def ROI(p):
                ingresos = p * ventas(p)
                return (ingresos - costo_total) / costo_total



            p0, p1 = float(request.POST.get('p0')), float(request.POST.get('p1'))
            precio_optimo, iteraciones = USecante.metodo_secante(ROI, p0, p1)
            roi                        = f'{(ROI(precio_optimo) * -100):.2f}'
            cantidad_ventas            = f"{ventas(precio_optimo):2f}"


            print(f"El precio óptimo es: ${precio_optimo:.2f}", flush=True)
            print(f"El ROI en este punto es: {roi}", flush=True)
            print(f"La cantidad de ventas necesarias son: {cantidad_ventas}", flush=True)

            precios = np.linspace(0, 3000, 500)
            roi_values = ROI(precios)


            # # Extraemos las iteraciones para graficar
            # iter_precios, iter_rois = zip(*iteraciones)

            # # Creamos la gráfica
            # plt.figure(figsize=(12, 8))
            # plt.plot(precios, roi_values, label='ROI vs Precio', color='blue')
            # plt.axvline(x=precio_optimo, color='red', linestyle='--', label=f'Precio Óptimo: ${precio_optimo:.2f}')
            # plt.scatter(precio_optimo, ROI(precio_optimo), color='red')

            # # Graficamos las iteraciones
            # plt.plot(iter_precios, iter_rois, 'o-', color='green', label='Iteraciones')

            # # Añadimos etiquetas y título
            # plt.title('Retorno de Inversión (ROI) en función del Precio con Iteraciones del Método de la Secante')
            # plt.xlabel('Precio ($)')
            # plt.ylabel('ROI')
            # plt.legend()
            # plt.grid(True)



            # Guardar la imagen en un objeto BytesIO
            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            plt.close()
            print("Generando imagen")

            # response = HttpResponse(buf.getvalue(), content_type='image/png;base64')
            # response['Content-Disposition'] = 'attachment; filename="grafica.png"'

            # return response

            contexto = {
                'costo': costo_total,
                'precio_optimo': f"{precio_optimo:.2f}",
                'roi': roi,
                'iteraciones': iteraciones,
                'ventas': cantidad_ventas
            }
        except (ValueError, TypeError) as e:
            contexto = {
                'error_message': f"Error en los datos de entrada: {str(e)}"
            }

        return render(request, 'pages/ViewSecante/Index.html', contexto)

    return render(request, 'pages/ViewSecante/Index.html')


# V0 corresponde a la cantida de iteraciones máxima
# alpha Corresponde a la sensibilidad de las ventas
def ventas(p, V0=10000, alpha=0.01):
    return V0 * np.exp(-alpha * p)
