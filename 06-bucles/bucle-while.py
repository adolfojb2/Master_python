"""
#Bucle While
Es una estructura de control que itera o repite la ejecución
de una serie de instrucciones tantas veces como sea necesario hasta
que deje de cumplirse la condición.

contador
while <condición>:
    <Bloque de instrucciones>
    <actualización de contador>

"""

contador = 1
muestrame = str(0)
while contador <= 100:
    muestrame = muestrame + "," + str(contador)
    print(f"Estoy en el {contador}")
    contador += 1

print(muestrame)

#Ejemplo tabla de multiplicar
print("###### Ejemplo ######")
numero_usuario = int(input("¿Que tabla de multiplicar quieres?: "))
if numero_usuario <1:
    numero_usuario = 1
print(f"###Tabla de multiplicar del {numero_usuario}###")
contador = 1
while contador <=10:
    print(f"{numero_usuario} X {contador} = {numero_usuario*contador}")
    contador += 1
else:
    print("Tabla terminada.")    