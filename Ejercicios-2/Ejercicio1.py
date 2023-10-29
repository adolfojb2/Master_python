"""
Ejercicio1. Hacer un programa que tenga una lista de 8 números enteros
y haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer una función que recorra las listas de números y devuelva un string
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado) 
"""
#crear la lista
numeros = [13,64,52,73,21,7,91,63]

#Recorrer y mostrar

for numero in numeros:
    print(numero)
print("----------------------------------------------------")
def mostrarLista(lista):
    cadena = ""
    for elemento in lista:
        cadena += str(elemento)
        cadena += "\n" 
    return cadena
print(mostrarLista(numeros))

print("Ordenar y mostrar")
numeros.sort()
print(mostrarLista(numeros))

print("Mostrar su longitud")
print(len(numeros))

print("Busqueda en la lista")
busqueda = int(input("Ingrese el numero a buscar: "))

comprobar = isinstance(busqueda,int)
while not comprobar or busqueda <= 0:   
    busqueda = int(input("Ingrese el numero a buscar: "))
else:
    print(f"Has introducido el {busqueda}")

print(f"#### Buscar en la lista el número {busqueda} ####")
search = numeros.index(busqueda)
print(f"El número buscado existe en la lista y está en el índice {search}")        