class Venta:
    def __init__(self, numeroId: int, fecha: str, clienteId: int, vehiculoId: int, monto: int):
        self.numeroId = numeroId
        self.fecha = fecha
        self.clienteId = clienteId
        self.vehiculoId = vehiculoId
        self.monto = monto

    def establecerNumeroId(self, numeroId: int):
        self.numeroId = numeroId

    def establecerFecha(self, fecha: str):
        self.fecha = fecha

    def establecerClienteId(self, clienteId: int):
        self.clienteId = clienteId

    def establecerVehiculoId(self, vehiculoId: int):
        self.vehiculoId = vehiculoId

    def establecerMonto(self, monto: int):
        self.monto = monto

    def obtenerNumeroId(self) -> int:
        return self.numeroId

    def obtenerFecha(self) -> str:
        return self.fecha

    def obtenerClienteId(self) -> int:
        return self.clienteId

    def obtenerVehiculoId(self) -> int:
        return self.vehiculoId

    def obtenerMonto(self) -> int:
        return self.monto
