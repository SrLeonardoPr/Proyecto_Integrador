

# Importo la librería 'os' para poder limpiar la pantalla de la terminal
# y la función 'readkey' de la librería 'readchar' para leer teclas individualmente.
import os
from readchar import readkey

# Defino mi propia función llamada 'limpiar_terminal' para hacer más fácil la limpieza de la pantalla.
def limpiar_terminal():
    # Utilizo 'os.system()' para limpiar la terminal, dependiendo del sistema operativo.
    os.system('cls' if os.name == 'nt' else 'clear')

# Empiezo el núcleo de mi juego con una función llamada 'juego_terminal'.
def juego_terminal():
    # Pido al jugador que ingrese su nombre y lo uso en un mensaje de bienvenida.
    nombre_jugador = input("¡Hola! ¿Cómo estás? Antes de comenzar el emocionante juego, dime tu nombre: ")
    print(f"A partir de ahora, te llamaré {nombre_jugador}.")

    # Tengo un contador llamado 'numero' para seguir la secuencia numérica.
    numero = 0

    # Aquí empieza el bucle principal del juego.
    while numero <= 50:
        # Espero a que el jugador presione una tecla.
        tecla = readkey()

        # Si el jugador presiona la tecla de escape (ESC),
        # salgo del bucle infinito y el juego se detiene.
        if tecla == '\x1b':
            break
        
        # Si el jugador presiona la tecla de flecha hacia arriba (↑),
        # muestro un mensaje y también salgo del bucle.
        elif tecla == '\x1b[A':
            print("¡Presionaste la tecla ↑ (flecha hacia arriba)!")
            break
        
        # Si el jugador presiona cualquier otra tecla,
        # limpio la pantalla y muestro la tecla presionada junto con el número actual.
        else:
            limpiar_terminal()
            print(f"Presionaste la tecla: {tecla}")
            print(f"Número actual: {numero}")
            numero += 1  # Incremento el número para avanzar en la secuencia.

# Verifico si este archivo es el que se está ejecutando directamente.
if __name__ == "__main__":
    # Llamo a mi función 'juego_terminal' para comenzar el juego.
    juego_terminal()
    
