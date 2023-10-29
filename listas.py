
peliculas = []
nueva_pelicula = ''
while nueva_pelicula != 'parar':
    nueva_pelicula = input('Nueva pelicula: ')
    if nueva_pelicula != 'parar':
        peliculas.append(nueva_pelicula)


print('######## Listado de peliculas ##########')
for pelicula in peliculas:
    print(f'{peliculas.index(pelicula)+1}. {pelicula}')        



#reemplazar caracteres de una lista
#lista.replace("\","/")    