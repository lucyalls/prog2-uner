class Sucursal:
    def __init__(self, numeroId: int, direccion: str):
        self.numeroId = numeroId
        self.direccion = direccion
        self.ventas = []  

    def establecerNumeroId(self, numeroId: int):
        self.numeroId = numeroId

    def establecerDireccion(self, direccion: str):
        self.direccion = direccion

    def agregarVenta(self, venta):
        self.ventas.append(venta)

    def removerVenta(self, venta):
        if venta in self.ventas:
            self.ventas.remove(venta)

    def obtenerNumeroId(self) -> int:
        return self.numeroId

    def obtenerDireccion(self) -> str:
        return self.direccion

    def obtenerVentas(self):
        return self.ven