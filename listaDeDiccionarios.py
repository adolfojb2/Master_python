contactos = [

    {
        "nombre": "Adolfo",
        "email": "adolfo@gmail.com"
    },
    {
        "nombre": "Angelica",
        "email": "angie@gmail.com"
    },
    {
        "nombre": "Eduardo",
        "email": "eduardo@gmail.com"
    }
]

print(contactos[0]["nombre"])
contactos.append({"nombre":"Escaloni","email":"laEscaloneta@gmail.com"})
print("\n Lista de contactos:")

for contacto in contactos:
    print(f'Nombre: {contacto["nombre"]}')
    print(f'Email: {contacto["email"]}')
    print("\n")