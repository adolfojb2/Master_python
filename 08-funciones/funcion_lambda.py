"""
Se usan para tareas sencillas y sólo ocupan una linea de código.
"""
#lo que está antes de los dos puntos es el parámetro y los dos puntos funcionan como el return.
dime_el_year = lambda year: f'El año es {year}' 

print(dime_el_year(2023))

suma = lambda n1,n2: n1 + n2
resta = lambda numero1,numero2: numero1 - numero2
producto = lambda a,b:  a * b

print(suma(1,2))
print(resta(5,2))
print(producto(2,3))

#aplicaciones
par = lambda numero_a: numero_a % 2 == 0
print(par(1))
impar = lambda numero_b: numero_b % 2 != 0
print(impar(2))