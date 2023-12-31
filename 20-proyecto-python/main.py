"""
Proyecto Python y Mysql: 
- Abrir asistente
- Login o Registro
- Si elegimos registro, creará un usuario en la BD
- Si elegimos login, identifica al usuario y nos preguntará la constraseña
- Crear nota, mostrar notas, borrarlas.
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
    hazEl.login()