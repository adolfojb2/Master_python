"""
Elección del arrendatario
"""
carro = False
mascota = False
num_personas = 4
trabajo_fijo = True
discapacitados = False
aire = False

if carro == False and mascota == False and trabajo_fijo == True and discapacitados == False and num_personas <= 4:
    if aire:
        print("Puede arrendar pero como tiene aire debe pagar un excedente en el gasto de luz. ")
    else:
        print("Puede arrendar sin ningún problema.")    
else: 
    print("No cumple con las condiciones para arrendar.")        