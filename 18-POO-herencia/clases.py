#Herencia: es la posibilidad de compartir atributos y métodos entre clases.

class persona():
    def __init__(self, nombre, apellidos, altura, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.altura = altura
        self.edad = edad

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre    

    def getApellidos(self):
        return self.apellidos
    
    def setApellidos(self, apellidos):
        self.apellidos = apellidos
    
    def getAltura(self):
        return self.altura
    
    def setAltura(self, altura):
        self.altura = altura
    
    def getEdad(self):
        return self.edad
    
    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"
    
    def dormir(self):
        return "Estoy durmiendo"
    
class informatico(persona):
    def __init__(self):
        self.lenguajes = "HTML, Css, JavaScript, PHP"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando"