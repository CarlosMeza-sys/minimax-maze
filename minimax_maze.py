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

    def calcular_distancia(self, posicion1, posicion2): # Calcular distancia Manhattan
        distancia_f = abs(posicion1[0] - posicion2[0])
        distancia_c = abs(posicion1[1] - posicion2[1])
        return distancia_f + distancia_c

    def evaluar_mejor_paso(self, jugador):
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if jugador == 'raton':
            mejor_valor = -1
            posicion_actual = self.posicion_raton
            posicion_enemigo = self.posicion_gato
        else:
            mejor_valor = 999
            posicion_actual = self.posicion_gato
            posicion_enemigo = self.posicion_raton

        mejor_movimiento = posicion_actual
            
        for cambio in direcciones:
            nueva_f = posicion_actual[0] + cambio[0]
            nueva_c = posicion_actual[1] + cambio[1]
            nueva_posicion = (nueva_f, nueva_c)

            if 0 <= nueva_f < self.filas and 0 <= nueva_c < self.columnas:
                distancia = self.calcular_distancia(nueva_posicion, posicion_enemigo)

                if jugador == 'raton':
                    if distancia > mejor_valor:
                        mejor_valor = distancia
                        mejor_movimiento = nueva_posicion
                else:
                    if distancia < mejor_valor:
                        mejor_valor = distancia
                        mejor_movimiento = nueva_posicion
        return mejor_movimiento
    
    def jugar_turno(self, jugador):
        print(f'--- Turno del {jugador.capitalize()} ---')
        self.posicion_raton = self.evaluar_mejor_paso(jugador) if jugador == 'raton' else self.posicion_raton
        self.posicion_gato = self.evaluar_mejor_paso(jugador) if jugador == 'gato' else self.posicion_gato
        self.mostrar_tablero()

    def verificar_resultado(self):
        if self.posicion_raton == self.posicion_gato:
            return True
        return False
    
juego = Laberinto(5, 10)

for i in range(81): 
    if i < 31:
        print(f"\n--- El Ratón está en Modo Loco N° {i + 1} ---")
        juego.mover_raton_al_azar()
        juego.mostrar_tablero()
    else:
        # Turno del Ratón
        print(f"\n--- Turno {i - 30} ---")
        input('Presiona Enter para que se mueva el RATÓN 🐭...')
        juego.jugar_turno('raton')
        if juego.verificar_resultado(): # Verificar despues de cada movimiento
            print('¡EL RATÓN FUE ATRAPADO! Fin del juego.')
            break
        # Turno del Gato
        input ('Presiona Enter para que se mueva el GATO 😾...')
        juego.jugar_turno('gato')
        if juego.verificar_resultado(): # Verificar despues de cada movimiento
            print('¡EL GATO HA CAZADO! Fin del juego.')
            break