"""
Hacer un programa que pida números al usuario indefinidamente hasta 
meter el número 111.
"""

while True:    
    numero = int(input('Ingrese un número: '))
    if numero == 111:
        break
    else: 
        print(numero)
