class Sucursal:

    def __init__(self, numero_id: int, direccion: str):
        self.numero_id = numero_id
        self.direccion = direccion
        self.ventas = []

    def __eq__(self, otro):
        if not isinstance(otro, Sucursal):
            return False
        return self.obtener_numero_id() == otro.obtener_numero_id()

    def __str__(self):
        ventas_info = "\n".join([f"{str(venta)}" for venta in self.obtener_ventas()])

        info = (
            f"[SUCURSAL: ID={self.obtener_numero_id()}, Dirección: {self.obtener_direccion()}]\n"
            f"Ventas de esta sucursal:\n"
            f"{ventas_info if ventas_info else '(Sin ventas registradas)'}"
        )
        return info

    def establecer_numero_id(self, numero_id: int):
        self.numero_id = numero_id

    def establecer_direccion(self, direccion: str):
        self.direccion = direccion

    def agregar_venta(self, venta):
        self.ventas.append(venta)

    def remover_venta(self, venta):
        if venta in self.ventas:
            self.ventas.remove(venta)

    def obtener_numero_id(self):
        return self.numero_id

    def obtener_direccion(self):
        return self.direccion

    def obtener_ventas(self):
        return self.ventas