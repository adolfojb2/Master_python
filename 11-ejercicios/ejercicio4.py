"""
Ejercicio 4. Crear un script que tenga 4 variables, una lista, un string, un entero y un booleano y que
imprima un mensaje según el tipo de dato de cada variable. Usar funciones
"""
def traducir_tipo(tipo):
    resultado = None
    if tipo == list:
        resultado = "LISTA"
    elif tipo == str:
        resultado = "CADENA DE TEXTO"
    elif tipo == int:
        resultado = "ENTERO"
    elif tipo == bool:
        resultado = "BOOLEANO"
    return resultado                


def comprobar_tipado(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""                  
    if test:
        result = f"Este dato es del tipo {traducir_tipo(tipo)}"
    else:
        result = "El tipo de dato no es correcto"
    return result  

mi_lista = [1,2,3,4,5]
saludo = "hola mundo"
numero = 78
verdadero = True

print(comprobar_tipado(mi_lista, list))
print(comprobar_tipado(saludo, str))
print(comprobar_tipado(numero, int))
print(comprobar_tipado(verdadero, bool))