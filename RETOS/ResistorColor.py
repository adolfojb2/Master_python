"""
(Easy): Código para resistencias de precisión de 5 bandas
"""
bandas = [

    {
        "negro":0,
        "cafe":1,
        "rojo":2,
        "naranja":3,
        "amarillo":4,
        "verde":5,
        "azul":6,
        "morado":7,
        "gris":8,
        "blanco":9

    },
    {
        "negro":0,
        "cafe":1,
        "rojo":2,
        "naranja":3,
        "amarillo":4,
        "verde":5,
        "azul":6,
        "morado":7,
        "gris":8,
        "blanco":9
    },
    {
        "negro":0,
        "cafe":1,
        "rojo":2,
        "naranja":3,
        "amarillo":4,
        "verde":5,
        "azul":6,
        "morado":7,
        "gris":8,
        "blanco":9
    },
    {#multiplicadores
        "negro":1,
        "cafe":10,
        "rojo":100,
        "naranja":1000,
        "amarillo":10000,
        "verde":100000,
        "azul":1000000,
        "morado":10000000,
        "dorado":0.1,
        "plateado":0.01
    },
    {#tolerancias
        
        "cafe":1,
        "rojo":2,
        "verde":0.5,
        "azul":0.25,
        "morado":0.1,
        "gris":0.05
    }
]
def calcular_resistencia(b1,b2,b3,b4,b5):
    tres_bandas = str(bandas[0][b1]) + str(bandas[1][b2]) + str(bandas[2][b3])
    omhmios = int(tres_bandas) * bandas[3][b4]
    tolerancia = bandas[4][b5]
    return omhmios, tolerancia

resultado , tolerancia = calcular_resistencia("cafe","amarillo","morado","rojo","gris")
print(f"Resistencia: {resultado}")
print(f"Tolerancia: {tolerancia}%")