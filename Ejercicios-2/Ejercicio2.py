"""
Ejercicio 2. Escribir un programa que añada valores a una lista mientras
que su longitud sea menor a 120 y luego mostrar la lista.
"""
lista = []
contador = 1
#con while
"""
while contador <120:
    
    lista.append(contador)
    contador += 1
"""
#con for

for contador in range(0,120):
    lista.append(contador)


for elemento in lista:
    print(f"{lista.index(elemento)}. {elemento}")

print(lista)    