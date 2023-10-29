class coche:
    #Atributos o propiedades (variables)
    color = "rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    soy_publico = "Soy un atributo publico"
    __soy_privado = "Soy un atributo privado"

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
        
    def getPrivado(self):
        return self.__soy_privado
        
    #Métodos, son acciones que hace el objeto
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo            

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    
    def getInfo(self):
        info = "----- Información del coche -----"
        info += "\n Marca: " + self.marca
        info += "\n Modelo: " + self.modelo
        info += "\n Color: " + self.color
        info += "\n Caballaje: " + str(self.caballaje)
        info += "\n Plazas: " + str(self.plazas)
        info += "\n Velocidad: " + str(self.velocidad)
        
        return info
    