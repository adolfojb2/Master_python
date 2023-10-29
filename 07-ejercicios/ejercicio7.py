"""
Hacer un programa que muestre todos los números impares 
entre dos números que diga el usuario.
"""

numero1 = int(input('Valor de inicio: '))
numero2 = int(input('Valor del final: '))

if numero1 < numero2:
    for numero in range(numero1, (numero2 + 1)):
        if numero % 2 != 0:
            print(f'{numero} es impar.')
else:
    print('El primer número debe ser menor que el segundo.')