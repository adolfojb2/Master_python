"""
Escribe un programa en Python que realice las siguientes tareas:

1- Muestra el nombre y precio de cada producto en el diccionario.
2- Calcula el precio promedio de todos los productos y muestra el resultado.
3- Encuentra el producto más caro y muestra su nombre y precio.
4- Solicita al usuario que ingrese el nombre de un producto y muestra su precio, si el producto existe en el diccionario.
"""
productos = {
    "manzanas": 2.0,
    "platanos": 1.5,
    "naranjas": 3.0,
    "uvas": 2.5,
    "sandías": 5.0
}
sum_precios = 0
producto_mas_caro = ""
aux = 0
for producto in productos:
    print(f"Nombre: {producto}       Precio: {productos[producto]} " )
    sum_precios += productos[producto]
    if productos[producto] > aux:
        producto_mas_caro = producto
        aux = productos[producto]

prom_precios = sum_precios / len(productos)    
print(prom_precios)
print(f"El producto más caro es {producto_mas_caro} = {productos[producto]}")

nom_producto = input("Ingresa el nombre de un producto: ")
while not nom_producto in productos:
    print("El producto no está.")
    nom_producto = input("Ingresa el nombre de un producto: ")
else: 
    print(f"El precio de {nom_producto} es:{productos[nom_producto]}")   