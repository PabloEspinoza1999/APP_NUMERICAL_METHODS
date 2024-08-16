from datetime import datetime

class Cliente_Newton:
    def __init__(self, id, nombre_cliente, tiempo_respuesta, fecha_registro, correo, telefono, direccion, tipo_cliente, estado_cuenta, preferencias, comentarios):
        self.id = id
        self.nombre_cliente = nombre_cliente
        self.tiempo_respuesta = tiempo_respuesta
        self.fecha_registro = fecha_registro  
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.tipo_cliente = tipo_cliente
        self.estado_cuenta = estado_cuenta
        self.preferencias = preferencias
        self.comentarios = comentarios

class Cliente_NewtonData:
    def __init__(self):
        self.clientes = [
            Cliente_Newton(1, "Juan Perez Rodríguez", 10, datetime(2023, 1, 15), "juan.perez@mail.com", "555-1234", "Calle 1, San Jose, SJ, 10101", "Regular", "Activa", "Herramientas eléctricas", "Ninguno"),
            Cliente_Newton(2, "María González Mora", 5, datetime(2023, 2, 20), "maria.gonzalez@mail.com", "555-5678", "Calle 2, Alajuela, AL, 20101", "VIP", "Activa", "Pinturas y accesorios", "Problemas con entrega en la última compra"),
            Cliente_Newton(3, "Carlos Lopez Jimenez", 8, datetime(2023, 3, 5), "carlos.lopez@mail.com", "555-4321", "Calle 3, Heredia, HE, 30101", "Nuevo", "Activa", "Materiales de construcción", "Reclamó un producto dañado"),
            Cliente_Newton(4, "Sofía Fernández Paniagua", 6, datetime(2023, 4, 11), "sofia.fernandez@mail.com", "555-7111", "Calle 7, Puntarenas, PU, 60101", "Regular", "Activa", "Herramientas Manuales", "Satisfecha con el servicio"),
            Cliente_Newton(5, "Alejandro Vargas Chaves", 13, datetime(2023, 5, 2), "alejandro.vargas@mail.com", "555-8222", "Calle 8, Limón, LI, 70101", "VIP", "Activa", "Equipos de Protección Personal", "Ninguno"),
            Cliente_Newton(6, "Andrea Rojas Serrano", 4, datetime(2023, 5, 18), "andrea.rojas@mail.com", "555-9333", "Calle 9, Guanacaste, GU, 50101", "Nuevo", "Activa", "Materiales de Construcción", "Pedido llegó con retraso"),
            Cliente_Newton(7, "Ricardo Jimenez Salas", 7, datetime(2023, 6, 6), "ricardo.jimenez@mail.com", "555-1010", "Calle 10, Heredia, HE, 30101", "Regular", "Inactiva", "Herramientas Eléctricas", "No se le notificó la entrega"),
            Cliente_Newton(8, "Laura Ramírez Torres", 9, datetime(2023, 6, 15), "laura.ramirez@mail.com", "555-2020", "Calle 11, San Jose, SJ, 10111", "Regular", "Activa", "Pinturas y Accesorios", "Ninguno"),
            Cliente_Newton(9, "Jose Mendez Quesada", 11, datetime(2023, 6, 20), "jose.mendez@mail.com", "555-3030", "Calle 12, Alajuela, AL, 20111", "Regular", "Activa", "Herramientas Manuales", "Producto llegó dañado"),
            Cliente_Newton(10, "Mariana Sánchez Salazar", 3, datetime(2023, 7, 2), "mariana.sanchez@mail.com", "555-4040", "Calle 13, Cartago, CA, 40111", "VIP", "Activa", "Accesorios para el Hogar", "Ninguno"),
            Cliente_Newton(11, "Diego Herrera González", 12, datetime(2023, 7, 10), "diego.herrera@mail.com", "555-5050", "Calle 14, Heredia, HE, 30111", "Regular", "Activa", "Equipos de Protección Personal", "Satisfecho con el servicio"),
            Cliente_Newton(12, "Natalia Castro Blanco", 15, datetime(2023, 7, 18), "natalia.castro@mail.com", "555-6060", "Calle 15, San Jose, SJ, 10112", "Regular", "Inactiva", "Herramientas Eléctricas", "Reclamó un producto dañado"),
            Cliente_Newton(13, "Pablo Mora Chacon", 2, datetime(2023, 7, 21), "pablo.mora@mail.com", "555-7070", "Calle 16, Guanacaste, GU, 50111", "Nuevo", "Activa", "Materiales de Construcción", "Ninguno"),
            Cliente_Newton(14, "Carolina Ruiz Pacheco",8, datetime(2023, 7, 25), "carolina.ruiz@mail.com", "555-8080", "Calle 17, Cartago, CA, 40112", "VIP", "Activa", "Pinturas y Accesorios", "Ninguno"),
            Cliente_Newton(15, "Jorge Pineda Vargas", 5, datetime(2023, 7, 28), "jorge.pineda@mail.com", "555-9090", "Calle 18, Puntarenas, PU, 60111", "Regular", "Activa", "Equipos de Protección Personal", "Ninguno"),
            Cliente_Newton(16, "Valeria Gomez Ureña", 1, datetime(2023, 7, 30), "valeria.gomez@mail.com", "555-1111", "Calle 19, Limón, LI, 70111", "Regular", "Activa", "Accesorios para el Hogar", "Ninguno"),
        ]
        self.next_id = len(self.clientes) + 1

    def get_all_clientes(self):
        return self.clientes

    def add_cliente(self, cliente_data):
        # Convierte la fecha a datetime si no lo es
        fecha_registro = cliente_data.get("fecha_registro")
        if isinstance(fecha_registro, str):
            fecha_registro = datetime.strptime(fecha_registro, "%Y-%m-%d")

        cliente = Cliente_Newton(
            self.next_id,
            cliente_data["nombre_cliente"],
            cliente_data["tiempo_respuesta"],
            fecha_registro,
            cliente_data["correo"],
            cliente_data["telefono"],
            cliente_data["direccion"],
            cliente_data["tipo_cliente"],
            cliente_data["estado_cuenta"],
            cliente_data["preferencias"],
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
