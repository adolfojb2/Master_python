"""
Una función es un conjunto de instrucciones agrupadas bajo un nombre concreto 
que pueden reutilizarse invocando a la función tantas veces como sea necesario.

def NombreDeMiFuncion(parámetros):
    #Bloque de código

NombreDeMiFuncion(mi_parámetro)    
"""

#Ejemplo 1
print("#### Ejemplo 1 ####")
#Definir función
def muestra_nombre():
    print("Julian")
    print("Pedro")
    print("Gareth")
    print("\n")

#Invocar función
muestra_nombre()    

print("#### Ejemplo 2: Parámetros ####")
def mostrar_tu_nombre(nombre, edad):
    print(f"Tu nombre es {nombre}")
    if edad>=18:
        print("Y eres mayor de edad.")

mostrar_tu_nombre("Gareth",17)

print("#### Ejemplo 3 ####")
def tabla(numero):
    print(f"Tabla de multiplicar del número {numero}")

    for n in range(1,11):
        print(f"{numero} x {n} = {numero*n}")

    print("\n")    

numero = 5
tabla(numero)        

print("#### Ejemplo 3.1 ####")
#mostrar todas las tablas de multiplicar
for num_tabla in range(1,11):
    tabla(num_tabla)

print("#### Ejemplo 4 ####")
#parámetros opcionales    
def getEmpleado(nombre,dni = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Julian")   

print("\n#### Ejemplo 5 ####")
#return y parámetros opcionales
def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo
print(saludame("Adolfo"))  

print("\n#### Ejemplo 6 ####")
def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    divi = numero1 / numero2

    cadena = ""
    if basicas != False:
        cadena += "suma: " + str(suma)
        cadena += "\n"
        cadena += "resta: " + str(resta)
        cadena += "\n"
    else:    
        cadena += "multiplicación:" + str(multi)
        cadena += "\n"
        cadena += "división: " + str(divi)
        cadena += "\n"

    return cadena
print(calculadora(5,7,True))    

print("\n#### Ejemplo 7 ####")
#funciones dentro de otras
def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto    

def devuelve_todo(nombre,apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)   
    return texto

print(devuelve_todo("Adolfo","Betin Bracamontes"))