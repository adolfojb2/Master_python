"""
Diccionario: Es una estructura de datos que almacena un conjunto de datos en formato Calve : Valor.
Es parecido a un array asociativo o un objeto JSON.
"""

persona = {
    "nombre": "Adolfo",
    "Apellidos": "Betin Bracamontes",
    "edad": 27,
    "correo": "adolfojb2@gmail.com",
    "profesión": "Ingeniero Electrónico"
}
print(type(persona))
print(persona)
print(persona['nombre'])
print(persona['profesión'])

#Lista con diccionarios
contactos = [
    {
        'nombre': 'Antonio',
        'email': 'antonio@gmail.com'
    },
    {
        'nombre': 'Carla',
        'email': 'carla@gmail.com'
    },
    {
        'nombre': 'Robert',
        'email': 'robertboom@gmail.com'
    }
]

contactos[0]['nombre'] = 'Heisenberg'
contactos[0]['email'] = 'heisenberg@gmail.com'
print(contactos[0]['nombre'])

print("\nListado completo de contactos: ")
print("-------------------------------------")
for contacto in contactos:
    print(contacto['nombre'])
    print(contacto['email'])
    print("-------------------------------------")
   