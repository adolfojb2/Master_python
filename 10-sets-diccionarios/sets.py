"""
SET: Es un tipo de dato, para tener una colección de valores que no tiene índice ni orden.
"""
personas = {"Adolfo","Jose","Maldini"}
personas.add("Albert")
personas.remove("Maldini")
print(type(personas))
print(personas)


"""
*************** Metodos de los sets *******************
union_set = set1.union(set2)
print(union_set)  # Resultado: {1, 2, 3, 4, 5}

interseccion_set = set1.intersection(set2)
print(interseccion_set)  # Resultado: {3}

diferencia_set = set1.difference(set2)
print(diferencia_set)  # Resultado: {1, 2}

diferencia_simetrica_set = set1.symmetric_difference(set2)
print(diferencia_simetrica_set)  # Resultado: {1, 2, 4, 5}
"""