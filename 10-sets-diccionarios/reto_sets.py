"""
Escribe un programa en Python que encuentre los elementos comunes entre 'lista1' y 'lista2' utilizando sets,
 y luego muestre esos elementos en un nuevo set llamado 'elementos_comunes'.
"""

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

set1 = set(lista1)
set2 = set(lista2)

elementos_comunes = set1.intersection(set2)

print(elementos_comunes)