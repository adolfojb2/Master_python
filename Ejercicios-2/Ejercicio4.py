"""
Ejercicio 4. Crear un script que tenga 4 variables, una lista, un string, un entero
y un booleano y que imprima un mensaje según el tipo de dato de cada variable.
"""
def traducir_tipo(tipo):
    result = None
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result = "STRING"
    elif tipo == int:
        result = "ENTERO"
    elif tipo == bool:
        result = "BOOLEANO"   
    return result             

def comprobar_tipado(dato, tipo):
    test = isinstance(dato,tipo)
    result = ""
    if test:
        result = f"Este dato es del tipo {traducir_tipo(tipo)}"
    else:
        result = "El tipo de dato no es correcto"
    return result        

mi_lista = ["Hola mundo", 26]
texto = "Master en Python"
numero = 127
verdadero = True

print(comprobar_tipado(mi_lista,list))
print(comprobar_tipado(texto,str))
print(comprobar_tipado(numero,int))
print(comprobar_tipado(verdadero,bool))