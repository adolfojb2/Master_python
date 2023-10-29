def tabla(numero):
    print(f'Tabla de multiplicar del número {numero}')

    for contador in range(11):
        operacion = numero * contador
        print(f'{numero} x {contador} = {operacion}')

    print('\n')    


for segundo in range(1,11):
    tabla(segundo)