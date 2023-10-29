"""
Ejercicio 5. Crear una lista con el contenido de esta tabla:
ACCION      AVENTURA            DEPORTES
GTA         ASSASSINS            FIFA 23
COD          CRASH               PRO 23
PUGB       Prince of Persia      MOTO GP 23

Mostrar esta información ordenada.
"""

tabla = [
    {
        "categoria": "Accion",
        "juegos": ["GTA","COD","PUGB"]
    },
    {
        "categoria": "Aventura",
        "juegos": ["ASSASSINS","CRASH","Prince of Persia"],
    },
    {
        "categoria": "Deportes",
        "juegos": ["FIFA 23", "PRO 23","MOTO GP 23"]
    }
]

for categoria in tabla:
    print(f"---------- {categoria['categoria']} ---------------")
    for juego in categoria['juegos']:
        print(juego)