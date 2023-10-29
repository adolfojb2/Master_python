"""
Una variable es un contenedor de información 
que dentro guarda un dato, se pueden crear muchas variables
y que cada una tenga un dato distinto.

Python es un lenguaje débilmente tipado, no hay que definir las variables.
"""
#crear variable es asignarles un valor
texto = "Master en python"
print(texto)
numero = 26
decimal = 7.3
print(decimal)
decimal_nuevo = decimal + 5
print(decimal_nuevo)

print("----------------------------------")
#Concatenación
nombre = "Adolfo"
apellidos = "Betin Bracamontes"
web = "adolfobetin.com.co"
print(nombre +" "+apellidos+" - "+web )
print(f"{nombre} {apellidos} -> {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre,apellidos,web))

print(nombre,apellidos,web) #esto no es concatenar