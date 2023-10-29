"""
Mostrar todas las tablas de multiplicar del 1 al 10, mostrando el 
titulo de la tabla y luego las multiplicaciones del 1 al 10.
"""

for numero1 in range(1,11):
    print(f'Tabla del {numero1}')
    for numero2 in range(1,11):
        print(f'{numero1} X {numero2} = {numero1*numero2}')
    print('\n')    