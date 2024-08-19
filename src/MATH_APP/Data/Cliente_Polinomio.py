from decimal import Decimal

class Cliente_Polinomio:
    def __init__(self, id, nombre_cliente, nombre_producto, precio, satisfaccion_cliente):
        self.id = id
        self.nombre_cliente = nombre_cliente
        self.nombre_producto = nombre_producto
        self.precio = precio
        self.satisfaccion_cliente = satisfaccion_cliente

class Cliente_PolinomioData:
    def __init__(self):
        self.clientes = [
            Cliente_Polinomio(1, "Ana Gómez", "Smartphone XYZ", 100, 3.5),
            Cliente_Polinomio(2, "Luis Martínez", "Laptop Pro 15", 200, 4.0),
            Cliente_Polinomio(3, "Maria Rodríguez", "Tablet Air", 300, 4.2),
            Cliente_Polinomio(4, "Carlos Pérez", "Smartwatch Z", 400, 4.1),
            Cliente_Polinomio(5, "Laura López", "Auriculares Bose", 500, 3.9),
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
