class Contacto:
    def __init__(self,nombre,telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}, Numero: {self.telefono}"