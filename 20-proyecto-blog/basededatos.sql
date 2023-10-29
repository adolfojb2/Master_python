CREATE DATABASE IF NOT EXISTS blog;
use blog;

-- Tabla de Usuarios
CREATE TABLE Usuarios (
    user_id INT(25) PRIMARY KEY AUTO_INCREMENT NOT NULL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_usuarios PRIMARY KEY(user_id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

-- Tabla de Artículos
CREATE TABLE Articulos (
    article_id INT(25) PRIMARY KEY AUTO_INCREMENT NOT NULL,
    titulo VARCHAR(200) NOT NULL,
    contenido TEXT NOT NULL,
    fecha_publicacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    autor_id INT(25),
    CONSTRAINT pk_articulos PRIMARY KEY(article_id),
    CONSTRAINT uq_titulo UNIQUE(titulo),
    FOREIGN KEY (autor_id) REFERENCES Usuarios(user_id)
)ENGINE=InnoDb;

-- Tabla de Comentarios
CREATE TABLE Comentarios (
    comment_id INT(25) PRIMARY KEY AUTO_INCREMENT NOT NULL,
    contenido TEXT NOT NULL,
    fecha_comentario TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    autor_id INT(25),
    article_id(25) INT,
    CONSTRAINT pk_comentarios PRIMARY KEY(comment_id),
    CONSTRAINT fk_comentario_usuario FOREIGN KEY (autor_id) REFERENCES Usuarios(user_id),
    CONSTRAINT fk_comentario_producto FOREIGN KEY (article_id) REFERENCES Articulos(article_id)
)ENGINE=InnoDb;
