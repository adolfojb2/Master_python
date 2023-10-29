from coche import coche

carro = coche("Amarillo", "Renault", "Clio", 150, 200, 4)
carro1 = coche("Negro", "Chevrolet", "Camaro SS", 300, 400, 2)
carro2 = coche("Rojo", "Lamborghini", "Gallardo", 350, 320, 2)
carro3 = coche("Gris", "Hundai", "Tuccson", 120, 180, 4)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

print(carro.soy_publico)
#print(carro.__soy_privado)
print(carro.getPrivado())

#Detectar tipado
if type(carro) == coche:
    print("Es un objeto correcto")
else:
    print("No es un objeto correcto!!")


#Visibilidad