"""
Proyecto Integrador - Python
Este proyecto ha sido creado como parte del programa de estudio en ADA school y representa el esfuerzo y dedicación del estudiante en el aprendizaje de Python y su aplicación en proyectos reales.

"""
## Version 5.1 del proyecto integrador 
## Status FINALIZADO ACTUALIZADO. Utilizacion de la funcion map() y reduce().
import os
import random
from functools import reduce

class Juego:
    def __init__(self, mapa_str):
        self.mapa = self.parsear_mapa(mapa_str)
        self.pos_inicial = (0, 0)
        self.pos_final = (len(self.mapa[0]) - 1, 20)
        self.px, self.py = self.pos_inicial
        self.mapa[self.py][self.px] = 'P'

    def parsear_mapa(self, mapa_str):
        mapa_filas = list(map(list, mapa_str.strip().split("\n")))
        return mapa_filas

    def limpiar_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_mapa(self):
        for fila in self.mapa:
            print(''.join(fila))

    def mover_jugador(self, dx, dy):
        nueva_px, nueva_py = self.px + dx, self.py + dy

        if (
            0 <= nueva_px < len(self.mapa[0]) and
            0 <= nueva_py < len(self.mapa) and
            self.mapa[nueva_py][nueva_px] != '#'
        ):
            self.mapa[self.py][self.px] = '.'
            self.px, self.py = nueva_px, nueva_py
            self.mapa[self.py][self.px] = 'P'
            self.limpiar_terminal()
            self.mostrar_mapa()
        else:
            self.limpiar_terminal()
            self.mostrar_mapa()
            print("Movimiento inválido")

class JuegoArchivo(Juego):
    def __init__(self, mapa_folder):
        nombre_archivo = random.choice(os.listdir(mapa_folder))
        path_completo = os.path.join(mapa_folder, nombre_archivo)
        with open(path_completo, 'r') as archivo:
            mapa_str = reduce(lambda x, y: x + y, archivo.readlines(), '')
        super().__init__(mapa_str)

if __name__ == "__main__":
    juego = JuegoArchivo("mapas") 
    juego.mostrar_mapa()

    while (juego.px, juego.py) != juego.pos_final:
        tecla = input("Presiona una tecla (W = arriba, S = abajo, A = izquierda, D = derecha, Q = salir): ").upper()

        if tecla == 'Q':
            break
        elif tecla == 'W':
            juego.mover_jugador(0, -1)
        elif tecla == 'S':
            juego.mover_jugador(0, 1)
        elif tecla == 'A':
            juego.mover_jugador(-1, 0)
        elif tecla == 'D':
            juego.mover_jugador(1, 0)

            