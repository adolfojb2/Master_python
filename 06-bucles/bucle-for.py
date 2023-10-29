"""
#FOR
elemento_iterable: lista, rango, tupla

for <variable> in <elemento_iterable>:
    Bloque de instrucciones
"""
resultado = 0
for contador in range(1,6):
    print("Voy por el " + str(contador))
    resultado += contador
print(f"Resultado: {resultado}")    

#Ejemplo tablas de multiplicar
print("###### Ejemplo 1 ######")
numero_usuario = int(input("¿De que número quieres ver la tabla?: "))
if numero_usuario <1:
    numero_usuario = 1
print(f"TABLA del {numero_usuario}")
for numero_tabla in range(1,11):
    print(f"{numero_usuario} X {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla Finalizada.")    