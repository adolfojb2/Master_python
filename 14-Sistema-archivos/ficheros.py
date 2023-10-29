from io import open 
import pathlib
import shutil

#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
#print(f"La ruta es: {ruta}")
archivo = open(ruta,"a+")

#Escribir
archivo.write("****** Soy un texto metido desde python*******\n")

#cerrar archivo
archivo.close()

#Abir/leer archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta,"r")   #r: permiso de lectura

#leer contenido
# contenido = archivo_lectura.read()
# print(contenido)

#leer contenido y guardarlo en una lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

print(lista)

for frase in lista:
    lista_frase = frase.split()
    print(lista_frase)
    print(frase.upper())

#copiar archivo
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa = "C:/Users/BetinBracamontes/OneDrive - Universidad del Magdalena/PYTHON/Master_Python_udemy/14-Sistema-archivos/fichero_copiado.txt"
shutil.copyfile(ruta_original,ruta_alternativa)

#mover
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/14-Sistema-archivos/fichero_copiado_NUEVO.txt"
shutil.move(ruta_original,ruta_nueva)

#Eliminar
import os
ruta_nueva = str(pathlib.Path().absolute()) + "/14-Sistema-archivos/fichero_copiado_NUEVO.txt"
os.remove(ruta_nueva)

#comprobar si existe
import os.path
ruta_comprobar = os.path.abspath("./") + "/14-Sistema-archivos/fichero_copiado.txt"
print(ruta_comprobar)
if os.path.isfile(ruta_comprobar):
    print("El archivo existe.")
else:
    print("El archivo no existe.")    
