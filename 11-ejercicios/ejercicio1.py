"""
Ejercicio 1. Hacer un programa que tenga una lista de 8 números enteros y haga lo siguiente:
- Recorrer la lista y mostrarla (luego crear la función para ello)
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algún elemento (que el usuario pida por teclado)
"""
#Crear lista
numeros = [4,3,7,6,2,1,2,2]

# Crear una función que recorra una lista y devuelva el string
def mostrar_lista(lista):
    resultado = ""
    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"
    return resultado    
#Recorrer y mostrar
string_lista = mostrar_lista(numeros)
print(string_lista)

# Ordenarla y mostrarla
numeros.sort()
print(mostrar_lista(numeros))    

#mostrar su longitud
print(len(numeros))

#buscar algún elemento que el usuario pida por teclado
busqueda = int(input("Buscar: "))
comprobar = isinstance(busqueda,int)
while not comprobar or busqueda <=0:
    busqueda = int(input("Buscar: ")) 
else: 
    print(f"Has introducido el {busqueda}")

print(f"### Buscar en la lista el número {busqueda} ###")
search = numeros.index(busqueda)
print(f"El número buscado existe en la lista, es el indice {search}")        