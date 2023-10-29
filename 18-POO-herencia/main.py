import clases

persona = clases.persona("Adolfo","Betin","180","27")

persona.setNombre("Adolfo")
persona.setApellidos("Betin Bracamontes")
persona.setAltura("180 cm")
persona.setEdad("27 años")

print(persona.getNombre(), persona.getApellidos())
print(persona.hablar())