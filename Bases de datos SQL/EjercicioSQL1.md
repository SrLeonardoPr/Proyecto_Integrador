# Ejercicio base de datos SQL con PostgreSQL
## Ejercicio Agregaciones 

1. Crea una tabla llamada estudiantes con las columnas nombre (VARCHAR), edad (INTEGER) y puntuacion (DECIMAL).

2. Inserta 10 filas de datos en la tabla.

| nombre       | edad | puntuación |
|--------------|------|------------|
| Estudiante1  | 20   | 85.5       |
| Estudiante2  | 21   | 75.0       |
| Estudiante3  | 19   | 92.5       |
| Estudiante4  | 22   | 80.2       |
| Estudiante5  | 20   | 88.9       |
| Estudiante6  | 21   | 76.8       |
| Estudiante7  | 19   | 94.2       |
| Estudiante8  | 22   | 82.1       |
| Estudiante9  | 20   | 87.3       |
| Estudiante10 | 21   | 77.6       |

3. Realiza una consulta para obtener la puntuación promedio de los estudiantes mayores de 20 años.

4. Realiza una consulta para obtener el nombre de los estudiantes cuya puntuación sea mayor a 85 y la edad sea menor a 22.

5. Realiza una consulta para obtener la edad y la cantidad de estudiantes por cada edad. Ordena los resultados por edad de forma descendente.

6. Realiza una consulta para obtener la edad promedio de los estudiantes que tienen una puntuación mayor a 80, redondea el resultado a dos decimales con ROUND(<promedio>, 2), dónde <promedio> corresponde al valor promedio calculado en tu sentencia SELECT.

### Solucion
1. Creación de la tabla estudiantes
```sql
CREATE TABLE estudiantes (
    id serial PRIMARY KEY,
    nombre varchar(255),
    edad INT,
    puntuacion decimal(10,2)
);
```

2. Inserción de datos en la tabla estudiantes
```sql
INSERT INTO estudiantes(nombre, edad, puntuacion)
VALUES 
    ('Estudiante1', 20, 85.5),
    ('Estudiante2', 21, 75.0),
    ('Estudiante3', 19, 92.5),
    ('Estudiante4', 22, 80.2),
    ('Estudiante5', 20, 88.9),
    ('Estudiante6', 21, 76.8),
    ('Estudiante7', 19, 94.2),
    ('Estudiante8', 22, 82.1),
    ('Estudiante9', 20, 87.3),
    ('Estudiante10', 21, 77.6);
```

3. Consulta para obtener la puntuación promedio de los estudiantes mayores de 20 años
```sql
SELECT AVG(puntuacion) AS promedio_puntuacion
FROM estudiantes
WHERE edad > 20;
```

4. Consulta para obtener el nombre de los estudiantes cuya puntuación sea mayor a 85 y la edad sea menor a 22
```sql
SELECT nombre 
FROM estudiantes
WHERE puntuacion > 85 AND edad < 22;
```

5. Consulta para obtener la edad y la cantidad de estudiantes por cada edad, ordenando los resultados por edad de forma descendente
```sql
SELECT edad, COUNT(nombre) AS c_nombres
FROM estudiantes
GROUP BY edad 
ORDER BY edad DESC;
```
6. Consulta para obtener la edad promedio de los estudiantes que tienen una puntuación mayor a 80, redondeando el resultado a dos decimales
```sql
SELECT ROUND(AVG(edad), 2) AS p_edad
FROM estudiantes
WHERE puntuacion > 80;
```