import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def newton_raphson_optimize_cost(Tiempos, lambda_param=0.1, tol=1e-10, max_iter=100):
    T_prom = sum(Tiempos) / len(Tiempos)
    
    def cost_function(T):
        return (T - T_prom)**2 + lambda_param * T**2 + 0.1 * (T - T_prom)**3
    
    def cost_derivative(T):
        return 2 * (T - T_prom) + 2 * lambda_param * T + 0.3 * (T - T_prom)**2
    
    def cost_second_derivative(T):
        return 2 + 2 * lambda_param + 0.6 * (T - T_prom)
    
    T = T_prom
    Ruta = []  
    
    for i in range(max_iter):
        f_T = cost_derivative(T)
        f_prime_T = cost_second_derivative(T)
        T_new = T - f_T / f_prime_T
        
        Ruta.append({'iteracion': i + 1, 'valor': T})
        if abs(T_new - T) < tol:
            break
        
        T = T_new
    
    def generate_plot_image():
        T_values = np.linspace(min(Tiempos), max(Tiempos), 100)
        cost_values = [cost_function(T) for T in T_values]
        
        plt.figure(figsize=(10, 6))
        plt.plot(T_values, cost_values, label='Función de Costo')
        plt.axvline(x=T, color='r', linestyle='--', label=f'Tiempo Óptimo: {T:.2f}')
        plt.xlabel('Tiempo de Respuesta')
        plt.ylabel('Costo')
        plt.title('Optimización de Costo con Newton-Raphson')
        plt.legend()
        plt.grid(True)
        
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()
        
        plot_image_data = base64.b64encode(buf.getvalue()).decode('utf-8')
        return plot_image_data

    plot_image_data = generate_plot_image()

    return T, plot_image_data, Ruta
