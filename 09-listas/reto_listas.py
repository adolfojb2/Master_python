"""
El desafío consiste en escribir un programa que tome una lista de números como entrada y devuelva una nueva 
lista que contenga solo los números pares de la lista original.

Puedes seguir estos pasos para completar el reto:

1) Pide al usuario que ingrese una lista de números separados por espacios.
2) Convierte la entrada en una lista de números.
3) Filtra los números pares y crea una nueva lista que contenga solo esos números.
4) Imprime la nueva lista.
"""
def obtener_numeros_pares(lista_numeros):
    lista = []
    for numero in lista_numeros:
        if int(numero) % 2 == 0:
            lista.append(numero)
    return lista
        
numeros = input("Ingresa una lista de números separados por espacios: ")
lista_numeros = numeros.split()
print(lista_numeros)
print(type(lista_numeros))

new_list = obtener_numeros_pares(lista_numeros)

print(new_list)    