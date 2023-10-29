"""
Son las listas que se encuentran dentro de otras listas.
"""

contactos = [
    [
        'Luis',
        'Luis@gmail.com'
    ],
    [
        'Carlos',
        'carlos@gmail.com'
    ],
    [
        'Maria Jose',
        'mariajose@gmail.com'
    ]
]

#print(contactos[2][1])
#forma 1
for contacto in contactos:
    for elemento in contacto:
        print(elemento)
    print('\n')    
#forma 2
for contacto in contactos:
    print(f'{contacto[0]} -> {contacto[1]}')    
    print('\n')

#forma 3
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print(f'Nombre: {elemento}')
        elif contacto.index(elemento) == 1:
            print(f'Correo: {elemento}')    
    print('\n')     