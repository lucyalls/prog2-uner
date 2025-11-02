class Venta:
    def __init__(self, numero_id: int, fecha: str, cliente_id: int, vehiculo_id: int, monto: int):
        self.numero_id = numero_id
        self.fecha = fecha
        self.cliente_id = cliente_id
        self.vehiculo_id = vehiculo_id
        self.monto = monto

    def __eq__(self, otro):
        if not isinstance(otro, Venta):
            return False
        return self.obtener_numero_id() == otro.obtener_numero_id()

    def __str__(self):
        info = (
            f"[VENTA: ID={self.obtener_numero_id()}, "
            f"Fecha={self.obtener_fecha()}, "
            f"ClienteID={self.obtener_cliente_id()}, "
            f"VehiculoID={self.obtener_vehiculo_id()}, "
            f"Monto=${self.obtener_monto()}]"
        )
        return info

    def establecer_numero_id(self, numero_id: int):
        self.numero_id = numero_id

    def establecer_fecha(self, fecha: str):
        self.fecha = fecha

    def establecer_cliente_id(self, cliente_id: int):
        self.cliente_id = cliente_id

    def establecer_vehiculo_id(self, vehiculo_id: int):
        self.vehiculo_id = vehiculo_id

    def establecer_monto(self, monto: int):
        self.monto = monto

    def obtener_numero_id(self):
        return self.numero_id

    def obtener_fecha(self):
        return self.fecha

    def obtener_cliente_id(self):
        return self.cliente_id

    def obtener_vehiculo_id(self):
        return self.vehiculo_id

    def obtener_monto(self):
        return self.monto
