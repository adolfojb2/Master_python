#importar modulo
import sqlite3

#conexión / crear base de datos
conexion = sqlite3.connect('./19-BasesDeDatos/pruebas.db')

#crear cursor
cursor = conexion.cursor()

#crear tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    titulo VARCHAR(255),
    descripcion TEXT,
    precio INT(255)
);
""")

#Guardar cambios
conexion.commit()

#Insertar datos
"""
cursor.execute('INSERT INTO productos VALUES (null, "Segundo producto", "Descripción de mi producto 2", 350000)')
conexion.commit()
"""
#Borrar registros
cursor.execute('DELETE FROM productos') #borra toda la tabla 
conexion.commit()

#Insertar muchos registros de golpe
productos = [
    ("PC Gamer","Buena PC",3400000),
    ("Moto Mt09","Buena moto",15000000),
    ("Chevrolet Camaro SS","Buen carro",500000000),
    ("RTX 5000","Buena tarjeta gráfica",6700000)
]
cursor.executemany('INSERT INTO productos VALUES(null, ?,?,?)',productos)
conexion.commit()

#Update
cursor.execute('UPDATE productos SET precio=4000000 WHERE precio>3000000')
conexion.commit()

#Listar datos /lectura de datos
cursor.execute('SELECT * FROM productos')
productos = cursor.fetchall() #lista de tuplas donde cada tupla contiene una fila de la tabla.
for producto in productos:
    print("Titulo: ",producto[1])
    print("Descripción: ",producto[2])
    print("Precio: $",producto[3])
    print("\n")

#Otra lectura
cursor.execute('SELECT titulo FROM productos')
producto = cursor.fetchone() #primer elemento en una tupla
print(producto)

#cerrar conexión
conexion.close()
