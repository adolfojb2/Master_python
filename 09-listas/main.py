"""
Listas (Arrays): Son colecciones o conjuntos de datos/valores, bajo un único nombre.
Para acceder a esos valores podemos usar un índice numérico.
"""

#definir lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(("Mono zabaleta","Elder Dayan","Karen Lizarazo"))
years = list(range(1996,2024))
variada = ["Victor",30,2.8,True,"Texto"]
"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""
#Indices
print(peliculas[1])
print(peliculas[-2])
print(cantantes[0:2])
print(peliculas[1:]) #todos los elementos de la lista a partir del índice 1

#reasignar elementos de la lista
peliculas[0] = "Oppenheimer"
peliculas[1] = "La teoría del todo"
print(peliculas)
"""
#Añadir elementos a lista
peliculas.append("Megalodon")
print(peliculas)
#Bucle para agregar elementos a la lista
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input(" Nueva pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)
#Recorrer lista
print("********* LISTADO DE PELICULAS ********")
for pelicula in peliculas:
    print(f"* {peliculas.index(pelicula)}. {pelicula}")
"""
#listas multidimensionales
print("\n******************* Listado de contactos ************************") 
contactos = [
    [
        'Antonio',
        'antonio21@gmail.com'
    ],
    [
        'Luisa',
        'luisa@gmail.com'
    ],
    [
        'Wilber',
        'wilber01@gmail.com'
    ]
]   
print("Nombre      Correo ")
for contacto in contactos:
    print(f"{contacto[0]}      {contacto[1]}")
#print(contactos[2][1])