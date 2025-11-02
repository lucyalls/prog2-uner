class ServicioClientes:
    def __init__(self, servicio_concesionarias):
        self.servicio_concesionarias = servicio_concesionarias

    def obtener_total_ventas_por_cliente(self, concesionaria_id, cliente_id):
        
        concesionaria = self.servicio_concesionarias.obtener_por_id(concesionaria_id)
        
        if concesionaria is None:
            return 0
        
        cliente_encontrado = None
        for cliente in concesionaria.obtener_clientes():
            if cliente.obtener_numero_id() == int(cliente_id):
                cliente_encontrado = cliente
                break

        if cliente_encontrado is None:
            return 0
        
        total_ventas = 0
        for sucursal in concesionaria.obtener_sucursales():
            for venta in sucursal.obtener_ventas():
                if venta.obtener_cliente_id() == int(cliente_id):
                    total_ventas += venta.obtener_monto()
        
        return total_ventas