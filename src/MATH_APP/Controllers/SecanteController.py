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
            def roi_function(price, units_sold, total_cost):
                ingresos = units_sold * price
                ganancia_neta = ingresos - total_cost
                return ganancia_neta / total_cost


            def target_function(price):
                return roi_function(price, units_sold, total_cost) - target_roi


            # Usando el método de la secante para encontrar el precio óptimo
            # Queremos un ROI del 30% (0.3)
            roi =  float(request.POST.get('roi'))
            target_roi = roi / 100

            # Número de unidades esperadas a vender y costo total de desarrollo
            units_sold = float(request.POST.get('unidades'))
            total_cost = float(request.POST.get('costo_total'))


            # Propuestas iniciales de precios
            x0 = float(request.POST.get('p0'))
            x1 = float(request.POST.get('p1'))


            precio_optimo, iteraciones = USecante.secant_method(target_function, x0, x1)
            required_units_sold = total_cost * (1 + target_roi) / precio_optimo

            # Mostrar el precio óptimo
            print(f"El precio óptimo que genera un ROI del { roi }%: ${precio_optimo:.2f}", flush=True)

            # Mostrar la cantidad de iteraciones y los valores obtenidos en cada una
            print("\nIteraciones del método de la secante:")
            for i, val_x0, val_x1 in iteraciones:
                print(f"Iteración {i}: x0 = {val_x0:.2f}, x1 = {val_x1:.2f}", flush=True)

            print(f"La cantidad de ventas necesarias son: {required_units_sold}", flush=True)

            #precios = np.linspace(0, 3000, 500)
            #roi = roi_function(precios)


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
            #buf = BytesIO()
            #plt.savefig(buf, format='png')
            #buf.seek(0)
            #plt.close()
            #print("Generando imagen")

            # response = HttpResponse(buf.getvalue(), content_type='image/png;base64')
            # response['Content-Disposition'] = 'attachment; filename="grafica.png"'

            # return response

            contexto = {
                'costo'         : total_cost,
                'precio_optimo' : f"{precio_optimo:.2f}",
                'roi'           : roi,
                'iteraciones'   : iteraciones,
                'ventas'        : required_units_sold
            }

        except (ValueError, TypeError) as e:
            contexto = {
                'error_message': f"Error en los datos de entrada: {e}"
            }

        return render(request, 'pages/ViewSecante/Index.html', contexto)

    return render(request, 'pages/ViewSecante/Index.html')
