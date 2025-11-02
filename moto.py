import vehiculo


class Moto(vehiculo.Vehiculo):

    def __init__(
        self, numero_id, marca, modelo, anio, sucursal_id, estado_id, cilindrada
    ):
        super().__init__(numero_id, marca, modelo, anio, sucursal_id, estado_id)
        self.__cilindrada = cilindrada

    def __str__(self):
        info_padre = (
            f"ID: {self.obtener_numero_id()}, "
            f"Marca: {self.obtener_marca()}, "
            f"Modelo: {self.obtener_modelo()}, "
            f"Año: {self.obtener_anio()}, "
            f"Sucursal ID: {self.obtener_sucursal_id()}, "
            f"Estado ID: {self.obtener_estado_id()}"
        )
        info_moto = f"Cilindrada: {self.obtener_cilindrada()}"
        return f"[MOTO: {info_padre} | {info_moto}]"

    def establecer_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def obtener_cilindrada(self):
        return self.__cilindrada
