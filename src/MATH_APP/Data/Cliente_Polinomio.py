from decimal import Decimal

class Cliente_Polinomio:
    def __init__(self, id, nombre_cliente, precio, satisfaccion_cliente):
        self.id = id
        self.nombre_cliente = nombre_cliente
        self.precio = Decimal(precio)
        self.satisfaccion_cliente = Decimal(satisfaccion_cliente)

# Simular una base de datos en memoria
class Cliente_PolinomioData:
    def __init__(self):
        self.clientes = [
            Cliente_Polinomio(1,  "Ana Gómez",          250.20,  2.50),
            Cliente_Polinomio(2,  "Luis Martínez",      350.45,  5.00),
            Cliente_Polinomio(3,  "Maria Rodríguez",    280.20,  4.20),
            Cliente_Polinomio(4,  "Carlos Pérez",       400.20,  3.70),
            Cliente_Polinomio(5,  "Laura López",        200.30,  4.00),
            Cliente_Polinomio(6,  "Jorge Díaz",         320.50,  3.50),
            Cliente_Polinomio(7,  "Patricia Fernández", 299.99,  4.90),
            Cliente_Polinomio(8,  "Antonio Gómez",      149.98,  4.10),
            Cliente_Polinomio(9,  "Carmen González",    189.80,  3.50),
            Cliente_Polinomio(10, "Ricardo Sánchez",    150.99,  4.60),
            Cliente_Polinomio(1, 'Ana Gómez', 395.69, 3.61),
            Cliente_Polinomio(2, 'Luis Martínez', 148.49, 1.6),
            Cliente_Polinomio(3, 'Maria Rodríguez', 201.54, 3.22),
            Cliente_Polinomio(4, 'Carlos Pérez', 115.89, 2.34),
            Cliente_Polinomio(5, 'Laura López', 393.07, 4.9),
            Cliente_Polinomio(6, 'Jorge Díaz', 317.11, 3.85),
            Cliente_Polinomio(7, 'Patricia Fernández', 462.44, 3.58),
            Cliente_Polinomio(8, 'Antonio Gómez', 400.73, 4.84),
            Cliente_Polinomio(9, 'Carmen González', 317.72, 3.81),
            Cliente_Polinomio(10, 'Ricardo Sánchez', 119.96, 1.71),
            Cliente_Polinomio(11, 'Isabel Ramírez', 484.44, 2.25),
            Cliente_Polinomio(12, 'Pablo Herrera', 244.78, 1.01),
            Cliente_Polinomio(13, 'Andrea Torres', 250.03, 1.53),
            Cliente_Polinomio(14, 'Sergio Jiménez', 138.09, 1.04),
            Cliente_Polinomio(15, 'Marta García', 486.99, 1.36),
            Cliente_Polinomio(16, 'Enrique Morales', 409.26, 4.42),
            Cliente_Polinomio(17, 'Sofía Rivera', 375.57, 2.73),
            Cliente_Polinomio(18, 'Manuel Ortiz', 389.77, 1.43),
            Cliente_Polinomio(19, 'Elena Castillo', 355.13, 3.42),
            Cliente_Polinomio(20, 'Pedro Vargas', 417.68, 3.32),
            Cliente_Polinomio(21, 'Gloria Pérez', 386.53, 2.82),
            Cliente_Polinomio(22, 'David Fernández', 332.53, 3.7),
            Cliente_Polinomio(23, 'Rosa Mendoza', 322.3, 3.91),
            Cliente_Polinomio(24, 'Alberto Martínez', 426.62, 4.11),
            Cliente_Polinomio(25, 'Silvia Ruiz', 430.42, 4.56),
            Cliente_Polinomio(26, 'Raúl González', 113.21, 2.07),
            Cliente_Polinomio(27, 'Carolina Ramírez', 276.21, 1.88),
            Cliente_Polinomio(28, 'Oscar García', 317.41, 4.71),
            Cliente_Polinomio(29, 'Irene Martínez', 119.78, 1.34),
            Cliente_Polinomio(30, 'Francisco Sánchez', 103.91, 2.52),
            Cliente_Polinomio(31, 'Julia Torres', 328.92, 3.97),
            Cliente_Polinomio(32, 'Victor Ramírez', 257.92, 1.85),
            Cliente_Polinomio(33, 'Monica Herrera', 298.63, 4.39),
            Cliente_Polinomio(34, 'Alejandro Ruiz', 196.46, 4.48),
            Cliente_Polinomio(35, 'Lucía Sánchez', 172.97, 4.71),
            Cliente_Polinomio(36, 'Daniel Pérez', 406.85, 1.15),
            Cliente_Polinomio(37, 'Sara Rodríguez', 386.24, 1.12),
            Cliente_Polinomio(38, 'Hugo Morales', 140.17, 1.19),
            Cliente_Polinomio(39, 'Clara López', 480.75, 2.53),
            Cliente_Polinomio(40, 'Fernando Díaz', 480.05, 4.16),
            Cliente_Polinomio(41, 'Paula González', 203.62, 2.06),
            Cliente_Polinomio(42, 'Nuria Hernández', 364.59, 4.3),
            Cliente_Polinomio(43, 'Andrés Herrera', 241.13, 3.22),
            Cliente_Polinomio(44, 'Verónica Mendoza', 338.82, 3.54),
            Cliente_Polinomio(45, 'Iván Jiménez', 242.96, 2.59),
            Cliente_Polinomio(46, 'Ángel Ortiz', 280.59, 2.81),
            Cliente_Polinomio(47, 'Lorena Martínez', 415.87, 1.55),
            Cliente_Polinomio(48, 'Rubén Morales', 430.58, 2.49),
            Cliente_Polinomio(49, 'Esther Sánchez', 337.59, 1.71),
            Cliente_Polinomio(50, 'Gabriel Ramírez', 116.13, 3.03)
        ]
        self.next_id = len(self.clientes) + 1

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
