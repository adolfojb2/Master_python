cantantes = ['Mike towers','Shakira','Carlos vives','Fonseca']
numeros = [1, 3, 5, 7, 5, 4, 9]

#ordenar
print(numeros)
numeros.sort()
#numeros.sort(reverse=True)  #Ordenarlos de forma inversa
print(numeros)


#Añadir elementos
cantantes.append('Dua Lipa')
cantantes.insert(2,'Manuel Turizo')
print(cantantes)

#Eliminar elementos
cantantes.pop(4)
cantantes.remove('Mike towers')
print(cantantes)

#Dar la vuelta
cantantes.reverse()
print(cantantes)

#Buscar dentro de la lista
print('Dua Lipa' in cantantes)

#Contar elementos
print(f"Cantidad de elementos: {len(cantantes)}")

#Cuantas veces aparece un elemento en la lista
print(numeros.count(5))

#Conseguir indice
print("Indice:", end=" ")
print(cantantes.index('Carlos vives'))

#Unir listas
cantantes.extend(numeros)
print(cantantes)

#Borrar todos los elementos de una lista
numeros.clear()
print(numeros)