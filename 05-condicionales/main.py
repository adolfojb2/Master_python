"""
if condicion:
    instrucciones
else:
    otras instrucciones    
"""
print("#### Ejemplo 1 ####")
color = "azul"
if color == "negro":
    print("El color es negro.")
elif color == "azul":
    print("El color es azul.")
else: 
    print("Color incorrecto")        

print("#### Ejemplo 2 ####")
year = 2021
if year >= 2021:
    print("Estamos de 2021 en adelante.")    
else:
    print("Es un año anterior a 2021")    

print("#### Ejemplo 3 ####")   
nombre = "Adolfo Betin" 
ciudad = "Barcelona"
continente = "Europa"
edad = 18
mayoria_edad = 18
if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad") 
    if continente != "Europa":
        print("No es Europeo.")
    else:
        print(f"Es Europeo y es de la ciudad {ciudad}")    
else:
    print(f"{nombre} NO es mayor de edad")    

print("#### Ejemplo 4 elif ####")     
dia = 4
if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miércoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana.")                    

print("#### Ejemplo 5 ####")
edad_minima = 18
edad_maxima = 65
edad_official = 66 
if edad_official >=edad_minima and edad_official <= edad_maxima:
    print("Tiene la edad para trabajar")
else: 
    print("No tiene la edad para trabajar")        

print("#### Ejemplo 6 ####")    
# pais = "Colombia"

# if pais=="Mexico" or pais == "España" or pais == "Colombia":
#     print(f"{pais} es un pais de habla hispana.")
# else: 
#     print(f"{pais} No es un pais de habla hispana. :(")    

print("#### Ejemplo 7 not ####")
# pais = "Mexico"

# if not (pais=="Mexico" or pais == "España" or pais == "Colombia"):
#     print(f"{pais} NO es un pais de habla hispana.")
# else: 
#     print(f"{pais} Si es un pais de habla hispana. :(")      

print("#### Ejemplo 8 != ####") 
pais = "Francia"

if pais!="Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un pais de habla hispana.")
else: 
    print(f"{pais} Si es un pais de habla hispana. :(")   