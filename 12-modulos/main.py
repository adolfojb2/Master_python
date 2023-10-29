"""
MÓDULOS
Una forma de empaquetar nuestro código en módulos o librerias para así poder reutilizar esas funcionalidades tantas veces como necesitemos
y en cualquier parte del programa.
Definición: Funcionalidades ya hechas para reutilizar.
Módulos que ya vienen con python: https://docs.python.org/3/py-modindex.html
- Tambien podemos crear nuestros propios módulos.
"""

#importar módulo propio completo
#import mimodulo
#importar una función de mi módulo
#from mimodulo import holamundo
#importar todas las funciones del mi módulo y que se puedan llamar directamente
from mimodulo import *
print(holamundo("Adolfo José Betin Bracamontes"))

#módulo de fechas
import datetime
print(datetime.date.today())
fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print(fecha_personalizada)
print(datetime.datetime.now().timestamp())

#módulo de matemáticas
import math
print("La raiz cuadrada de 10: ", math.sqrt(10))
print("Número PI: ",math.pi)
print("Redondear hacia el mayor: ",math.ceil(3.567))
print("Redondear hacia el menor: ", math.floor(3.567))
print("Seno de 45 (radianes):", math.sin(45)) 


#Módulo random
import random
print("Número aleatorio entre 5 y 30: ",random.randint(5,30))

