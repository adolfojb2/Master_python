"""
¿cuanto es el x por ciento de X número?
ejemplo: 20% de 150
"""

numero = int(input('Introduce un número: '))
porcentaje = int(input(f'¿Que porcentaje quieres sacar de {numero}?: '))

resultado = numero * (porcentaje/100)

print(f'el {porcentaje} % de {numero} es {resultado}')