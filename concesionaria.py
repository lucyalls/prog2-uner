class Concesionaria:

    def __init__(self, numero_id, nombre):
        self.__numero_id = numero_id
        self.__nombre = nombre
        self.__clientes = []
        self.__sucursales = []
        self.__vehiculos = []

    def __eq__(self, otro):
        if not isinstance(otro, Concesionaria):
            return False
        return self.obtener_numero_id() == otro.obtener_numero_id()

    def __str__(self):
        
        info = (
            f"CONCESIONARIA: {self.obtener_nombre()} (ID: {self.obtener_numero_id()})\n"
        )

        info += "\nCLIENTES:\n"
        clientes_info = "\n".join([str(cliente) for cliente in self.obtener_clientes()])
        info += clientes_info if clientes_info else "  (Sin clientes registrados)"
        info += "\n"

        info += "\nSUCURSALES:\n"
        sucursales_info = "\n".join([str(sucursal) for sucursal in self.obtener_sucursales()])
        info += sucursales_info if sucursales_info else "  (Sin sucursales registradas)"
        info += "\n"

        info += "\nVEHÍCULOS (Inventario Total):\n"
        vehiculos_info = "\n".join([str(vehiculo) for vehiculo in self.obtener_vehiculos()])
        info += vehiculos_info if vehiculos_info else "  (Sin vehículos registrados)"
        info += "\n"

        return info

    def establecer_numero_id(self, numero_id):
        self.__numero_id = numero_id

    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def agregar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def remover_cliente(self, cliente):
        self.__clientes.remove(cliente)

    def agregar_sucursal(self, sucursal):
        self.__sucursales.append(sucursal)

    def remover_sucursal(self, sucursal):
        self.__sucursales.remove(sucursal)

    def agregar_vehiculo(self, vehiculo):
        self.__vehiculos.append(vehiculo)

    def remover_vehiculo(self, vehiculo):
        self.__vehiculos.remove(vehiculo)

    def obtener_numero_id(self):
        return self.__numero_id

    def obtener_nombre(self):
        return self.__nombre

    def obtener_clientes(self):
        return self.__clientes

    def obtener_sucursales(self):
        return self.__sucursales

    def obtener_vehiculos(self):
        return self.__vehiculos
