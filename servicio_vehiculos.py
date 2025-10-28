class ServicioVehiculos:
 def __init__(self, servicioConcesionarias):
     self.servicioConcesionarias = servicioConcesionarias
 def obtener_vehiculos_por_sucursal_y_estado(self, concesionaria_id, sucursal_id, estado_id):
        concesionaria = self.servicioConcesionarias.obtenerPorId(concesionaria_id)
        if concesionaria is None:
            return []
        sucursalEncontrada = None
        for sucursal in concesionaria.sucursales:
            if sucursal.numero_id == sucursal_id:
                sucursalEncontrada = sucursal
                break
        if sucursalEncontrada is None:
            return []
        resultado = []
        for vehiculo in sucursalEncontrada.vehiculos:
            if vehiculo.estado.id == estado_id:
                resultado.append(vehiculo)
        return resultado
        
