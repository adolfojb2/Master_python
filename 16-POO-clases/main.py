
#Definir una clase (molde para crear más objetos de ese tipo)
class coche:
    #Atributos o propiedades (variables)
    color = "rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

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
    
    

#Crear objeto / instanciar la clase
print("Coche 1:")
micoche = coche()        
print(micoche.color)
print("Velocidad actual: ",micoche.getVelocidad())
micoche.acelerar()
micoche.acelerar()
micoche.frenar()
print("Velocidad nueva: ",micoche.getVelocidad())

print("Color actual: ",micoche.getColor())
micoche.setColor("amarillo")
print("Color nuevo: ",micoche.getColor())

print("-----------------------------")
#Crear más objetos
print("Coche 2:")
coche2 = coche()
coche2.setColor("Verde")
coche2.setModelo("Gallardo")
print(coche2.getMarca(),coche2.getModelo(),coche2.getColor())

print(type(coche2))
