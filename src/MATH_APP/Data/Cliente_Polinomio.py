from decimal import Decimal

class Cliente_Polinomio:
    def __init__(self, id, nombre_cliente, precio, satisfaccion_cliente):
        self.id = id
        self.nombre_cliente = nombre_cliente
        self.precio = precio
        self.satisfaccion_cliente = satisfaccion_cliente

class Cliente_PolinomioData:
    def __init__(self):
        self.clientes = []
        self.next_id = len(self.clientes) + 1


    def upate_clientes(self, clientes):
        self.clientes = clientes


    def get_all_clientes(self):
        return self.clientes

    def add_cliente(self, cliente_data):
        cliente = Cliente_Polinomio(
            self.next_id,
            cliente_data["nombre_cliente"],
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
    
    def clean(self):
        self.clientes = []
