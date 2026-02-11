import random

class Laberinto:
    # Dimensiones del tablero
    def __init__(self, filas = 5, columnas = 10):
        self.filas = filas
        self.columnas = columnas
        self.posicion_raton = (0, 0)    # Posicion inicial del raton
        self.posicion_gato = (filas - 1, columnas - 1)  # Posicion inicial del gato
        self.tablero = [['.' for _ in range(columnas)] for _ in range(filas)]   # Estructurar Tablero
    
    def mostrar_tablero(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                
                if (fila, columna) == self.posicion_raton:
                    print("🐭", end = " ")
                elif (fila, columna) == self.posicion_gato:
                    print("😾", end = " ")
                else:
                    print(self.tablero[fila][columna], end = " ")
            print()
    
    def mover_raton_al_azar(self):
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        cambio = random.choice(direcciones)     # Aleatoriedad de direcciones
        nueva_f = self.posicion_raton[0] + cambio[0]
        nueva_c = self.posicion_raton[1] + cambio[1]
        if 0 <= nueva_f < self.filas and 0 <= nueva_c < self.columnas:  # Validar posicion
            self.posicion_raton = (nueva_f, nueva_c)
        else:
            pass

juego = Laberinto(5, 10)

for i in range(20):
    print(f"\n--- Turno {i+1} ---")
    juego.mover_raton_al_azar()
    juego.mostrar_tablero()