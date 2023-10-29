import os

#crear carpeta
if not os.path.isdir("./14-Sistema-archivos/mi_carpeta"):
    os.mkdir("./14-Sistema-archivos/mi_carpeta")
else:
    print("Ya existe el directorio")    

#Eliminar
#os.rmdir("./14-Sistema-archivos/mi_carpeta")

#Copiar
# import shutil
# ruta_original ="./14-Sistema-archivos/mi_carpeta"
# ruta_nueva = "./14-Sistema-archivos/mi_carpeta_COPIADA"
# shutil.copytree(ruta_original,ruta_nueva)

# os.rmdir("./14-Sistema-archivos/mi_carpeta")
# os.rmdir("./14-Sistema-archivos/mi_carpeta_COPIADA")

print("Contenido de mi carpeta:")
contenido = os.listdir("./14-Sistema-archivos/mi_carpeta")
print(contenido)

for fichero in contenido:
    print("Fichero: ",fichero)