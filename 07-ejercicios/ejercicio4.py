"""
Pedir 2 números al usuario y hacer todas las operaciones básicas de una 
calculadora y mostrarlo por pantalla.
"""

numero1 = int(input('Ingresa el primer número: '))
numero2 = int(input('Ingresa el segundo número: '))

suma = numero1 + numero2
resta = numero1 - numero2
producto = numero1 * numero2
division = numero1 / numero2

print(f'suma: {suma}, resta: {resta}, multiplicación: {producto}, división: {division}')