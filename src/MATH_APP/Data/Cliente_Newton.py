from datetime import datetime

class Cliente_Newton:
    def __init__(self, id, nombre_cliente, tiempo_respuesta, fecha_registro, correo, telefono, comentarios):
        self.id               = id
        self.nombre_cliente   = nombre_cliente
        self.tiempo_respuesta = tiempo_respuesta
        self.fecha_registro   = fecha_registro
        self.correo           = correo
        self.telefono         = telefono
        self.comentarios      = comentarios


class Cliente_NewtonData:
    def __init__(self):
        self.clientes = []
        self.next_id = len(self.clientes) + 1

    def get_all_clientes(self):
        return self.clientes
    
    def upate_clientes(self, clientes):
        self.clientes = clientes

    def add_cliente(self, cliente_data):
        # Convierte la fecha a datetime si no lo es
        fecha_registro = cliente_data.get("fecha_registro")
        if isinstance(fecha_registro, str):
            fecha_registro = datetime.strptime(fecha_registro, "%Y-%m-%d")

        cliente = Cliente_Newton(
            cliente_data['ID'],
            cliente_data["nombre_cliente"],
            cliente_data["tiempo_respuesta"],
            fecha_registro,
            cliente_data["correo"],
            cliente_data["telefono"],
            cliente_data["direccion"],
            cliente_data["comentarios"]
        )
        self.clientes.append(cliente)
        self.next_id += 1
        return cliente

    def update_cliente(self, cliente_id, updated_data):
        for cliente in self.clientes:
            if cliente.id == cliente_id:
                for key, value in updated_data.items():
                    if hasattr(cliente, key):
                        if key == 'fecha_registro' and isinstance(value, str):
                            value = datetime.strptime(value, "%d/%m/%Y")  # Convierte si es una cadena
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
