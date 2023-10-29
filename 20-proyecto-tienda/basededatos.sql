CREATE DATABASE IF NOT EXISTS tienda;
use tienda;

CREATE TABLE usuarios(
id         int(25) auto_increment not null,
nombre     varchar(100),
apellidos   varchar(255),
email       varchar(255) not null,
password    varchar(255) not null,
fecha       date not null,
CONSTRAINT pk_usuarios PRIMARY KEY(id),
CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE productos(
id           int(25) auto_increment not null,
usuario_id   int(25) not null,
titulo       varchar(255) not null,
descripcion  MEDIUMTEXT,
precio       int(25) not null,
stock        int(25) not null,
fecha        date not null,
CONSTRAINT pk_notas PRIMARY KEY(id),
CONSTRAINT uq_titulo UNIQUE(titulo),
CONSTRAINT fk_producto_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;

CREATE TABLE ventas(
id           int(25) auto_increment not null,
usuario_id   int(25) not null,
producto_id  int(25) not null,
unidades        int(25) not null,
precio_venta       int(25) not null,
total        int(25) not null,
fecha        date not null,
CONSTRAINT pk_ventas PRIMARY KEY(id),
CONSTRAINT fk_venta_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id),
CONSTRAINT fk_venta_producto FOREIGN KEY(producto_id) REFERENCES productos(id)
)ENGINE=InnoDb;