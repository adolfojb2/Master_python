"""
El programa tiene que pedir la nota de 15 alumnos y sacar por pantalla 
cuantos han aprobado y cuantos han suspendido.
"""
numero_alumnos = int(input('Ingresa el número de alumnos: '))
aprobados = 0
suspendidos = 0
for alumno in range(1,(numero_alumnos + 1)):
    nota = int(input(f'Ingresa la nota del alumno {alumno}: '))
    if nota >= 5: 
        aprobados += 1
    elif nota <5:
        suspendidos += 1

print(f'Han aprodado {aprobados} alumnos y han suspendido {suspendidos}.')