class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calle = 1

    def estado(self):
        return f"{self.nombre}, estás en la calle {self.calle}"
    
    def moverse(self, velocidad):
        self.calle += velocidad



