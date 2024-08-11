# Data/Customer.py
from decimal import Decimal

class Customer:
    def __init__(self, id, nombre, cedula, correo, edad, precio, costo, cantidad_maxima_demandada, tasa_cambio_demanda_precio):
        self.id = id
        self.nombre = nombre
        self.cedula = cedula
        self.correo = correo
        self.edad = edad
        self.precio = Decimal(precio)
        self.costo = Decimal(costo)
        self.cantidad_maxima_demandada = Decimal(cantidad_maxima_demandada)
        self.tasa_cambio_demanda_precio = Decimal(tasa_cambio_demanda_precio)

# Simular una base de datos en memoria
class CustomerData:
    def __init__(self):
        self.customers = [
            Customer(1, "John Doe", "123456789", "john@example.com", 30, '100.00', '80.00', '200.00', '1.05'),
            Customer(2, "Jane Smith", "987654321", "jane@example.com", 25, '150.00', '120.00', '150.00', '1.10'),
            # Agregar más clientes según sea necesario
        ]
        self.next_id = len(self.customers) + 1

    def get_all_customers(self):
        return self.customers

    def add_customer(self, customer_data):
        customer = Customer(
            self.next_id,
            customer_data["nombre"],
            customer_data["cedula"],
            customer_data["correo"],
            customer_data["edad"],
            customer_data["precio"],
            customer_data["costo"],
            customer_data["cantidad_maxima_demandada"],
            customer_data["tasa_cambio_demanda_precio"]
        )
        self.customers.append(customer)
        self.next_id += 1
        return customer

    def update_customer(self, customer_id, updated_data):
        for customer in self.customers:
            if customer.id == customer_id:
                for key, value in updated_data.items():
                    if hasattr(customer, key):
                        setattr(customer, key, value)
                return customer
        return None

    def delete_customer(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                self.customers.remove(customer)
                return customer
        return None

