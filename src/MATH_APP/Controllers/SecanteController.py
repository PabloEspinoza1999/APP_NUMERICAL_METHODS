from django.shortcuts import render
import base64
from django.http import HttpResponse
from ..Utils import USecante
import matplotlib.pyplot as plt
from io import BytesIO


def ShowSecante(request):
    context = {'resultado' : None, 'iteraciones': None }
    return render(request, 'pages/ViewSecante/Index.html', context=context)



def SaveSecante(request):
    if request.method == 'POST':
        try:
            # Se obtiene el ROI especificado
            roi =  float(request.POST.get('roi'))
            target_roi = roi / 100

            # Número de unidades esperadas a vender y costo total de desarrollo
            units_sold = float(request.POST.get('unidades'))
            total_cost = float(request.POST.get('costo_total'))


            # Propuestas iniciales de precios
            x0 = float(request.POST.get('p0'))
            x1 = float(request.POST.get('p1'))


            def roi_function(price, units_sold, total_cost):
                ingresos = units_sold * price
                ganancia_neta = ingresos - total_cost
                return ganancia_neta / total_cost


            def target_function(price):
                return roi_function(price, units_sold, total_cost) - target_roi


            precio_optimo, iteraciones = USecante.secant_method(target_function, x0, x1)
            required_units_sold = total_cost * (1 + target_roi) / precio_optimo

            # Mostrar el precio óptimo
            print(f"El precio óptimo que genera un ROI del { roi }%: ${precio_optimo:.2f}", flush=True)

            # Mostrar la cantidad de iteraciones y los valores obtenidos en cada una
            print("\nIteraciones del método de la secante:")
            for i, val_x0, val_x1 in iteraciones:
                print(f"Iteración {i}: x0 = {val_x0:.2f}, x1 = {val_x1:.2f}", flush=True)

            print(f"La cantidad de ventas necesarias son: {required_units_sold}", flush=True)


            print("--------------------------------\n")
            print("Generando imagen")


            # Gráfica del método de la secante
            # Extraer las iteraciones en x e y
            x_vals = [x1 for _, _, x1 in iteraciones]
            y_vals = [target_function(x) for x in x_vals]

            plt.figure(figsize=(10, 6))
            plt.plot(x_vals, y_vals, 'o-', label='Iteraciones')
            plt.axhline(0, color='r', linestyle='--', label='ROI objetivo')

            # Marcar el punto de convergencia
            plt.scatter([precio_optimo], [target_function(precio_optimo)], color='g', zorder=5, label=f'Precio óptimo: ${precio_optimo:.2f}')

            plt.title('Convergencia del Método de la Secante')
            plt.xlabel('Precio')
            plt.ylabel('Función objetivo (f(p))')
            plt.legend()
            plt.grid(True)

            # Guardar la imagen en un objeto BytesIO
            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            plt.close()

            imagen = 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode('utf-8')

            contexto = {
                'costo'         : total_cost,
                'precio_optimo' : f"{precio_optimo:.2f}",
                'roi'           : roi,
                'iteraciones'   : iteraciones,
                'ventas'        : required_units_sold,
                'imagen'        : imagen
            }

        except (ValueError, TypeError) as e:
            contexto = {
                'error_message': f"Error en los datos de entrada: {e}"
            }

        return render(request, 'pages/ViewSecante/Index.html', contexto)

    return render(request, 'pages/ViewSecante/Index.html')
