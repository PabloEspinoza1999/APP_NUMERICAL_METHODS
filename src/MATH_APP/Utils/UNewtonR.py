def satisfaccion_cliente(precio, costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio):
    """
    Calcula la satisfacción del cliente en función del precio.
    """
    demanda = cantidad_maxima_demandada - tasa_cambio_demanda_precio * precio
    satisfaccion = demanda * (precio - costo)  # Modelo simplificado
    return satisfaccion

def derivada_satisfaccion_cliente(precio, costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio, delta=0.001):
    """
    Calcula la primera derivada de la satisfacción del cliente con respecto al precio.
    """
    return (satisfaccion_cliente(precio + delta, costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio) -
            satisfaccion_cliente(precio, costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio)) / delta

def segunda_derivada_satisfaccion_cliente(precio, costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio, delta=0.001):
    """
    Calcula la segunda derivada de la satisfacción del cliente con respecto al precio.
    """
    return (derivada_satisfaccion_cliente(precio + delta, costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio) -
            derivada_satisfaccion_cliente(precio, costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio)) / delta

def newton_raphson_precio(precio_inicial, costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio, tolerancia=0.01, max_iter=100):
    """
    Encuentra el precio óptimo que maximiza la satisfacción del cliente usando el método de Newton-Raphson.
    Devuelve el precio óptimo y la satisfacción en ese precio.
    """
    precio = precio_inicial
    ruta_punto_optimo = []

    for _ in range(max_iter):
        # Calcular satisfacción y sus derivadas
        satisfaccion = satisfaccion_cliente(precio, costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio)
        derivada = derivada_satisfaccion_cliente(precio, costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio)
        segunda_derivada = segunda_derivada_satisfaccion_cliente(precio, costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio)

        # Mostrar la satisfacción actual para fines de diagnóstico
        print(f"Precio actual: {precio:.2f}, Satisfacción: {satisfaccion:.2f}")

        # Agregar el precio y la satisfacción actual a la ruta de puntos óptimos
        ruta_punto_optimo.append((precio, satisfaccion))

        # Verificar si la segunda derivada es suficientemente pequeña
        if abs(segunda_derivada) < tolerancia:
            raise ValueError("Segunda derivada demasiado pequeña, el método puede no converger.")

        # Calcular el nuevo precio usando el método de Newton-Raphson
        precio_nuevo = precio - derivada / segunda_derivada

        # Verificar la convergencia
        if abs(precio_nuevo - precio) < tolerancia:
            satisfaccion_final = satisfaccion_cliente(precio_nuevo, costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio)
            ruta_punto_optimo.append((precio_nuevo, satisfaccion_final))
            return precio_nuevo, satisfaccion_final, ruta_punto_optimo

        # Actualizar el precio
        precio = precio_nuevo

    # Si no converge, se puede retornar None
    return None
