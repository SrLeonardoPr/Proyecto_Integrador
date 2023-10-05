-- Creacion de base de datos para el proyecto integrador de la academia ADA SCHOOL 
-- Proyecto realizado por Jose Leonardo Piñeres Ramirez

-- 1. Obtener el precio mínimo, precio máximo y precio promedio de todos los productos. 
-- Resultado en el archivo (queries_1.csv)

SELECT
    MIN(precio_unitario) AS precio_minimo,
    MAX(precio_unitario) AS precio_maximo,
    AVG(precio_unitario) AS precio_promedio
FROM
    Producto;

-- 2. Calcular la cantidad total de productos en stock por sucursal.
-- Resultado en el archivo (queries_2.csv)

SELECT
    s.id AS sucursal_id,
    s.nombre AS sucursal_nombre,
    SUM(st.cantidad) AS cantidad_total_en_stock
FROM
    Sucursal s
INNER JOIN
    Stock st ON s.id = st.sucursal_id
GROUP BY
    s.id, s.nombre;
  

-- 3. Obtener el total de ventas por cliente.
-- Resultado en el archivo (queries_3.csv)

SELECT
    c.id AS cliente_id,
    c.nombre AS cliente_nombre,
    SUM(i.monto_venta) AS total_ventas
FROM
    Cliente c
LEFT JOIN
    Orden o ON c.id = o.cliente_id
LEFT JOIN
    Item i ON o.id = i.orden_id
GROUP BY
    c.id, c.nombre;

