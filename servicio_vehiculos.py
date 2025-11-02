class ServicioVehiculos:
    def __init__(self, servicio_concesionarias):
        self.servicio_concesionarias = servicio_concesionarias

    def obtener_vehiculos_por_sucursal_y_estado(self, concesionaria_id, sucursal_id, estado_id):
        
        concesionaria = self.servicio_concesionarias.obtener_por_id(concesionaria_id)

        if concesionaria is None:
            return []
        
        sucursal_encontrada = None
        for sucursal in concesionaria.obtener_sucursales():
            if sucursal.obtener_numero_id() == int(sucursal_id):
                sucursal_encontrada = sucursal
                break

        if sucursal_encontrada is None:
            return []
        
        resultado = []
        for vehiculo in concesionaria.obtener_vehiculos():
            if (vehiculo.obtener_sucursal_id() == int(sucursal_id) and vehiculo.obtener_estado_id() == int(estado_id)):
                resultado.append(vehiculo)
                
        return resultado