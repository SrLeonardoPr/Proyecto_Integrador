-- Creacion de base de datos para el proyecto integrador de la academia ADA SCHOOL 
-- Proyecto realizado por Jose Leonardo Piñeres Ramirez

CREATE DATABASE Proyecto_Integrador_Postgres;

-- Tabla Categoria
CREATE TABLE Categoria (
    id serial PRIMARY KEY,
    nombre varchar(255) NOT NULL
);

-- Tabla Producto
CREATE TABLE Producto (
    id serial PRIMARY KEY,
    nombre varchar(255) NOT NULL,
    marca varchar(255),
    categoria_id int NOT NULL,
    precio_unitario decimal(10, 2) NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES Categoria(id)
);

-- Tabla Sucursal
CREATE TABLE Sucursal (
    id serial PRIMARY KEY,
    nombre varchar(255) NOT NULL,
    direccion text NOT NULL
);

-- Tabla Stock
CREATE TABLE Stock (
    id serial PRIMARY KEY,
    sucursal_id int NOT NULL,
    producto_id int NOT NULL,
    cantidad int NOT NULL,
    UNIQUE (sucursal_id, producto_id),
    FOREIGN KEY (sucursal_id) REFERENCES Sucursal(id),
    FOREIGN KEY (producto_id) REFERENCES Producto(id)
);

-- Tabla Cliente
CREATE TABLE Cliente (
    id serial PRIMARY KEY,
    nombre varchar(255) NOT NULL,
    telefono varchar(20)
);

-- Tabla Orden
CREATE TABLE Orden (
    id serial PRIMARY KEY,
    cliente_id int NOT NULL,
    sucursal_id int NOT NULL,
    fecha date NOT NULL,
    total decimal(10, 2) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Cliente(id),
    FOREIGN KEY (sucursal_id) REFERENCES Sucursal(id)
);

-- Tabla Item
CREATE TABLE Item (
    id serial PRIMARY KEY,
    orden_id int NOT NULL,
    producto_id int NOT NULL,
    cantidad int NOT NULL,
    monto_venta decimal(10, 2) NOT NULL,
    FOREIGN KEY (orden_id) REFERENCES Orden(id),
    FOREIGN KEY (producto_id) REFERENCES Producto(id)
);