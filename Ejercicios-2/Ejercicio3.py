"""
Ejercicio 3. Programa que compruebe si una variable está vacia y si está vacia, rellenarla con texto en minusculas 
y mostrarlo en mayusculas.
"""

texto = ""

if len(texto.strip()) <= 0:
    texto = "Texto en minúsculas"
    print(texto.upper())

else: 
    print("La variable no está vacía.")