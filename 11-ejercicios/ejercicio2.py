"""
Ejercicio 2. Escribir un programa que añada valores a una lista mientras que su longitud sea menor
a 120 y luego mostrar la lista.
Plus: Usar while y for.
"""

valores = []
"""
for valor in range(1,120):
    valores.append(valor)

print(valores)
"""
contador = 1
while contador <120:
    valores.append(contador)
    print(f"Elemento: {contador}")
    contador += 1

print(valores)    