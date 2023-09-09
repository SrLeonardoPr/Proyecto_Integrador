-- Crear la tabla "Categoria"
CREATE TABLE Categoria (
    id INTEGER PRIMARY KEY NOT NULL,
    nombre TEXT
);

-- Crear la tabla "Producto" con la relación a "Categoria"
CREATE TABLE Producto (
    id INTEGER PRIMARY KEY NOT NULL,
    nombre TEXT,
    marca TEXT,
    categoria_id INTEGER NOT NULL,
    precio_unitario REAL,
    FOREIGN KEY (categoria_id) REFERENCES Categoria(id)
);

-- Crear la tabla "Sucursal"
CREATE TABLE Sucursal (
    id INTEGER PRIMARY KEY NOT NULL,
    nombre TEXT,
    direccion TEXT
);

-- Crear la tabla "Stock" con restricción UNIQUE
CREATE TABLE Stock (
    id INTEGER PRIMARY KEY NOT NULL,
    sucursal_id INTEGER NOT NULL,
    producto_id INTEGER NOT NULL,
    cantidad INTEGER,
    UNIQUE(sucursal_id, producto_id),
    FOREIGN KEY (sucursal_id) REFERENCES Sucursal(id),
    FOREIGN KEY (producto_id) REFERENCES Producto(id)
);

-- Crear la tabla "Cliente"
CREATE TABLE Cliente (
    id INTEGER PRIMARY KEY NOT NULL,
    nombre TEXT,
    telefono TEXT
);

-- Crear la tabla "Orden" con relaciones a "Cliente" y "Sucursal"
CREATE TABLE Orden (
    id INTEGER PRIMARY KEY NOT NULL,
    cliente_id INTEGER NOT NULL,
    sucursal_id INTEGER NOT NULL,
    fecha DATE,
    total REAL,
    FOREIGN KEY (cliente_id) REFERENCES Cliente(id),
    FOREIGN KEY (sucursal_id) REFERENCES Sucursal(id)
);

-- Crear la tabla "Item" con relaciones a "Orden" y "Producto"
CREATE TABLE Item (
    id INTEGER PRIMARY KEY NOT NULL,
    orden_id INTEGER NOT NULL,
    producto_id INTEGER NOT NULL,
    cantidad INTEGER,
    monto_venta REAL,
    FOREIGN KEY (orden_id) REFERENCES Orden(id),
    FOREIGN KEY (producto_id) REFERENCES Producto(id)
);
