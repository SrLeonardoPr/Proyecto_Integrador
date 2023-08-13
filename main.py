"""
Proyecto Integrador - Python
Este proyecto ha sido creado como parte del programa de estudio en ADA school y representa el esfuerzo y dedicación del estudiante en el aprendizaje de Python y su aplicación en proyectos reales.

"""

import os
import readchar


def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_mapa(mapa):
    for fila in mapa:
        print(''.join(fila))

def juego_laberinto(mapa, pos_inicial, pos_final):
    px, py = pos_inicial
    mapa[py][px] = 'P'
    mostrar_mapa(mapa)
    
    while (px, py) != pos_final:
        tecla = readchar.readkey()
        nueva_px, nueva_py = px, py
        
        if tecla == '\x1b':
            break
        elif tecla == '\x1b[A':
            nueva_py -= 1
        elif tecla == '\x1b[B':
            nueva_py += 1
        elif tecla == '\x1b[C':
            nueva_px += 1
        elif tecla == '\x1b[D':
            nueva_px -= 1
        
        if (
            0 <= nueva_px < len(mapa[0]) and
            0 <= nueva_py < len(mapa) and
            mapa[nueva_py][nueva_px] != '#'
        ):
            mapa[py][px] = '.'
            px, py = nueva_px, nueva_py
            mapa[py][px] = 'P'
            limpiar_terminal()
            mostrar_mapa(mapa)
        else:
            limpiar_terminal()
            mostrar_mapa(mapa)
            print("Movimiento inválido")

if __name__ == "__main__":
    laberinto_str = (
        "..###################\n"
        "....#.....#.....#...#\n"
        "#.#.#.#######.#.###.#\n"
        "#.#.....#.#...#.....#\n"
        "###.#####.#######.#.#\n"
        "#.........#.......#.#\n"
        "#####.###.###.###.#.#\n"
        "#.#.....#.....#...#.#\n"
        "#.###########.###.#.#\n"
        "#.#...#.........#.#.#\n"
        "#.#.#.###.#######.#.#\n"
        "#.#.#...#.#.#...#.#.#\n"
        "#.#.#.#.#.#.#.#####.#\n"
        "#...#.#.......#...#.#\n"
        "#.#.#####.###.#.#####\n"
        "#.#.....#.#.......#.#\n"
        "#.#####.#.#.#.#.###.#\n"
        "#.#.....#.#.#.#.....#\n"
        "#####.#######.###.#.#\n"
        "#...........#...#.#.#\n"
        "###################.#\n"
    )

    laberinto_filas = laberinto_str.strip().split("\n")
    laberinto_matriz = [list(fila) for fila in laberinto_filas]

    pos_inicial = (20, len(laberinto_matriz) - 1)
    pos_final = (len(laberinto_matriz[0]) - 1, 0)

    juego_laberinto(laberinto_matriz, pos_inicial, pos_final)


