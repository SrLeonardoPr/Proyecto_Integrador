### Proyecto realizado por Jose Leonardo Piñeres Ramirez
# Proyecto Variables en Python

# Definir variables de cada tipo primitivo
entero = 10
flotante = 3.14
booleano = True
caracter = 'A'
cadena = 'Hola'

# Concatenar las variables en una cadena
resultado = cadena + str(entero) + str(flotante) + str(booleano) + caracter

# Imprimir el resultado
print(resultado)

# Límite de los enteros en Python
limite_enteros = 2**31 - 1  # El límite es 2^31 - 1 para enteros con signo
print("Límite de enteros:", limite_enteros)

# Límite de los flotantes en Python
limite_flotantes = 1.8e308  # El límite es aproximadamente 1.8 x 10^308
print("Límite de flotantes:", limite_flotantes)

# Fórmula para la suma de los primeros n números pares
n = 5 #Tambien se puede pedir por teclado con un input
suma_pares = n * (n + 1)  # La suma de los primeros n números pares es n * (n + 1)
print("Suma de los primeros", n, "números pares:", suma_pares)

## Fin de la tarea  Lun 3 Jul 2023
