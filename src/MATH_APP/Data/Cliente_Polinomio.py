from decimal import Decimal

class Cliente_Polinomio:
    def __init__(self, id, nombre_cliente, nombre_producto, precio, satisfaccion_cliente):
        self.id = id
        self.nombre_cliente = nombre_cliente
        self.nombre_producto = nombre_producto
        self.precio = Decimal(precio)
        self.satisfaccion_cliente = Decimal(satisfaccion_cliente)

# Simular una base de datos en memoria
class Cliente_PolinomioData:
    def __init__(self):
        self.clientes = [
            Cliente_Polinomio(1, "Ana Gómez", "Smartphone XYZ", '299.99', '4.5'),
            Cliente_Polinomio(2, "Luis Martínez", "Laptop Pro 15", '1299.00', '3.8'),
            Cliente_Polinomio(3, "Maria Rodríguez", "Tablet Air", '499.99', '4.2'),
            Cliente_Polinomio(4, "Carlos Pérez", "Smartwatch Z", '199.99', '4.7'),
            Cliente_Polinomio(5, "Laura López", "Auriculares Bose", '249.99', '4.0'),
            Cliente_Polinomio(6, "Jorge Díaz", "Cámara Digital Canon", '549.00', '3.5'),
            Cliente_Polinomio(7, "Patricia Fernández", "Televisor OLED 4K", '1499.00', '4.8'),
            Cliente_Polinomio(8, "Antonio Gómez", "Router WiFi 6", '149.99', '4.1'),
            Cliente_Polinomio(9, "Carmen González", "Impresora Láser HP", '189.99', '3.9'),
            Cliente_Polinomio(10, "Ricardo Sánchez", "Consola de Videojuegos", '399.99', '4.6'),
        ]
        self.next_id = len(self.clientes) + 1

    def get_all_clientes(self):
        return self.clientes

    def add_cliente(self, cliente_data):
        cliente = Cliente_Polinomio(
            self.next_id,
            cliente_data["nombre_cliente"],
            cliente_data["nombre_producto"],
            cliente_data["precio"],
            cliente_data["satisfaccion_cliente"]
        )
        self.clientes.append(cliente)
        self.next_id += 1
        return cliente

    def update_cliente(self, cliente_id, updated_data):
        for cliente in self.clientes:
            if cliente.id == cliente_id:
                for key, value in updated_data.items():
                    if hasattr(cliente, key):
                        setattr(cliente, key, value)
                return cliente
        return None

    def delete_cliente(self, cliente_id):
        for cliente in self.clientes:
            if cliente.id == cliente_id:
                self.clientes.remove(cliente)
                return cliente
        return None
