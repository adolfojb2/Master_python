# """
# Capturar excepciones y manejar errores en código susceptible a fallos/errores
# """
# try:
#     nombre = input("¿Cual es tu nombre?: ")
#     if len(nombre) > 1:
#         nombre_usuario = f"Tu nombre es: {nombre}"
#     print(nombre_usuario)

# except:
#     print("Ha ocurrido un error, mete bien el nombre.")

# else:
#     print("Todo ha funcionado correctamente.")   

# finally:
#     print("Fin de la iteración!!!")     

# numeros = [4,3,7,6,2,1,2,2]

# #buscar algún elemento que el usuario pida por teclado
# try: 
#     busqueda = int(input("Buscar: "))
#     comprobar = isinstance(busqueda,int)
#     while not comprobar or busqueda <=0:
#         busqueda = int(input("Buscar: ")) 
#     else: 
#         print(f"Has introducido el {busqueda}")

#     print(f"### Buscar en la lista el número {busqueda} ###")

#     search = numeros.index(busqueda)
#     print(f"El número buscado existe en la lista, es el indice {search}")   
# except:
#     print("El número no está en la lista.")         

#Multiples excepciones
"""
try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado es: "+str(numero*numero))   

except TypeError:
    print("Debes convertir tus cadenas a enteros!!")     

# except ValueError:
#     print("Introduce un número correcto.")    

except Exception as e:
    print("Ha ocurrido un error: ",type(e).__name__)    
"""
#Excepciones personalizadas o lanzar excepcion
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))
    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real.")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no está completo")
    else: 
        print(f"Bienvenido al master en python {nombre}!!!")
except ValueError:
    print("Introduce los datos correctamente.")        
except Exception as e:
    print("Existe un error: ",e)