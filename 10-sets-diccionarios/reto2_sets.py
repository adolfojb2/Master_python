"""
Escribe un programa en Python que encuentre los elementos únicos en cada lista individualmente y
luego muestre esos elementos en dos nuevos sets, uno para 'lista1' y otro para 'lista2', sin incluir 
los elementos que se repiten entre las dos listas.
"""

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

set1 = set(lista1)
set2 = set(lista2)

set1_unicos = set1.difference(lista2)
set2_unicos = set2.difference(lista1)

print(set1_unicos)
print(set2_unicos)