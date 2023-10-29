"""
Variables locales: Se definen dentro de la función y no se puede usar fuera de ella, sólo
estan disponibles dentro. A no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una función y están disponibles
dentro y fuera de ella.
"""
#variable global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres."
print(frase)
def hola_mundo():
    frase = "Hola mundo!!"
    print("Dentro de la función:")
    print(frase)

    year = 2023
    print(year)

    global website
    website ="www.google.com"
    print("Dentro: ",website)
    return "Dato devuelto" + str(year)

print(hola_mundo())    
print("Fuera: ",website)