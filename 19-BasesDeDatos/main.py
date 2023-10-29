import mysql.connector

#conexión
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"
)

#¿La conexión a sido correcta?
print(database)

#crear cursor
cursor = database.cursor(buffered=True)

#crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

#mostrar bases de datos
"""
cursor.execute("SHOW DATABASES")
for bd in cursor:
    print(bd)
"""
#crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)               
)
""")

#Ver tablas
"""cursor.execute("SHOW TABLES")
for tabla in cursor:
    print(tabla)"""

#Insertar 

cursor.execute("INSERT INTO vehiculos VALUES(null, 'Chevrolet', 'Camaro SS', 500)")
database.commit()

#Insertar muchos
vehiculos = [
    ("Hyundai","Tucson",700),
    ("Kia","Picanto",500),
    ("Renault","Sandero",450),
    ("Nissan","GTR 360",300),
    ("Ford","Fiesta",750)
]

"""cursor.executemany("INSERT INTO vehiculos VALUES(null, %s,%s,%s)",vehiculos)
database.commit()"""


#leer datos
cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()
for coche in result:
    print(coche[1],coche[2], coche[3])

"""cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()
print(coche)"""

#Eliminar datos
cursor.execute("DELETE FROM vehiculos WHERE id <= 70")
database.commit()
print(cursor.rowcount, "borrados!!") #numero de elementos eliminados

#Actualizar
cursor.execute("UPDATE vehiculos SET modelo='LEON' WHERE marca='Ford'")
database.commit()
print(cursor.rowcount, "Actualizados!!!")


#cerrar cursor y conexión
cursor.close()
database.close()