class Cliente:
    
    def __init__(self, numero_id: int, nombres: str, apellidos: str, email: str):
        self.numero_id = numero_id
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email

    def __eq__(self, otro):
        if not isinstance(otro, Cliente):
            return False
        return self.obtener_numero_id() == otro.obtener_numero_id()

    def __str__(self):
        info = (
            f"  [CLIENTE: ID={self.obtener_numero_id()}, "
            f"Nombre={self.obtener_nombres()} {self.obtener_apellidos()}, "
            f"Email={self.obtener_email()}]"
        )
        return info

    def establecer_numero_id(self, numero_id):
        self.numero_id = numero_id

    def establecer_nombres(self, nombres):
        self.nombres = nombres

    def establecer_apellidos(self, apellidos):
        self.apellidos = apellidos

    def establecer_email(self, email):
        self.email = email

    def obtener_numero_id(self):
        return self.numero_id

    def obtener_nombres(self):
        return self.nombres

    def obtener_apellidos(self):
        return self.apellidos

    def obtener_email(self):
        return self.email