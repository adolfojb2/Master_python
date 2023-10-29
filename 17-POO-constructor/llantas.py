class llanta():
    def __init__(self,marca,tama, presion):
        self.marca = marca
        self.tama = tama
        self.presion = presion
        self.agarre = []
    
    def set_marca(self, marca):
        self.marca = marca
    
    def get_marca(self):
        return self.marca
    
mi_llanta = llanta("Bringston",19,12)
print(mi_llanta.get_marca())    
mi_llanta.set_marca("Otra_marca")
print(mi_llanta.get_marca())  
mi_llanta.agarre.append("Ag1")
mi_llanta.agarre.append("Ag2")
mi_llanta.agarre.append("Ag3")
print(mi_llanta.agarre)