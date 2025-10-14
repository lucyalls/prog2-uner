# Ejercicio 3

import vehiculo

class Auto(vehiculo.Vehiculo):

    def __init__(self, numero_id, marca, modelo, anio, sucursal_id, estado_id, airbags, frenos_abs, caballos_fuerza):
        super().__init__(numero_id, marca, modelo, anio, sucursal_id, estado_id)

        self.__airbags = airbags
        self.__frenos_abs = frenos_abs
        self.__caballos_fuerza = caballos_fuerza

    def __eq__(self, otro_auto):
        pass

    def __str__(self):
        pass

    def establecer_airbags(self, airbags):
        self.__airbags = airbags

    def establecer_frenos_abs(self, frenos_abs):
        self.__frenos_abs = frenos_abs

    def establecer_caballos_fuerza(self, caballos_fuerza):
        self.__caballos_fuerza = caballos_fuerza

    def obtener_airbags(self):
        return self.__airbags
    
    def obtener_frenos_abs(self):
        return self.__frenos_abs
    
    def obtener_caballos_fuerza(self):
        return self.__caballos_fuerza


