"""
Ejercicio 5. Crear una lista con el contenido de esta tabla:
ACCION            AVENTURA            DEPORTES
GTA                ASSASINS             FIFA 22
COD                CRASH                PRO 22
PUGB              PRINCE OF PERSIA       MOTO GP 22
Mostrar esta información ordenada.
"""

tabla = [
    {
        "categoria":"accion",
        "juegos":["GTA","COD","PUGB"]
    },
    {
        "categoria":"aventura",
        "juegos":["Assasins","Crash","Prince of Persia"]
    },
    {
        "categoria":"deportes",
        "juegos":["FIFA 22","PRO 22","MOTO GP 22"]
    }
]

for diccionario in tabla:
    print(f"--------- {diccionario['categoria']}----------")
    for juego in diccionario['juegos']:
        print(juego)
        