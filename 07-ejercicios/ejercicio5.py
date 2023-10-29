"""
Hacer un programa que muestre todos los números entre dos números que 
diga el usuario.
"""

inicio = int(input('Ingresa el número de inicio: '))
fin = int(input('Ingresa el número del final: '))
if inicio<fin:

    for numero in range(inicio,(fin+1)):
        print(numero)

else: 
    print('El numero de inicio debe ser menor que el numero del final.')