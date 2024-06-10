def ganancias(costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio, precio):
    demanda = cantidad_maxima_demandada - tasa_cambio_demanda_precio * precio  
    ingresos = demanda * precio  
    return ingresos - costo * demanda  

             
def derivada_ganancias(precio, costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio, delta=0.001):
    return (ganancias(costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio, precio + delta) - ganancias(costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio, precio)) / delta


def newton_raphson_precio(precio, costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio, tolerancia=0.01, max_iter=100):
    ruta_punto_optimo = [];
    for _ in range(max_iter):
        ganancia = ganancias(costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio, precio)
        derivada = derivada_ganancias(precio, costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio)
        if abs(ganancia) < tolerancia:
            return ruta_punto_optimo;
        precio = precio - ganancia / derivada
        ruta_punto_optimo.append(precio)
        print(precio)
    return None


