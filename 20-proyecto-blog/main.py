"""
Blog con registro y login de usuarios, articulos y comentarios para los articulos.
- Login o registro
- Si elegimos registro, creará un usuario en la BD
- Si elegimos login, identifica al usuario y nos preguntará la constraseña
Opciones: 
- publicar articulo, ver articulos, comentar articulo, editar articulo, eliminar articulo, cerrar sesión.
"""
from usuarios import acciones
print("""
Acciones disponibles:
    - registro
    - login
""")
hazEl = acciones.Acciones()
accion = input("¿Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    None 
    #hazEl.login()