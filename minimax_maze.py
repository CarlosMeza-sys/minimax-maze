import random

class Laberinto:
    # Dimensiones del tablero
    def __init__(self, filas = 5, columnas = 10):
        self.filas = filas
        self.columnas = columnas
        self.posicion_raton = (0, 0)    # Posicion inicial del ratón
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
        # Validar posición para que no salga del tablero
        if 0 <= nueva_f < self.filas and 0 <= nueva_c < self.columnas:
            return (nueva_f, nueva_c)
        return self.posicion_raton

    # Heurística Manhattan
    def calcular_distancia(self, posicion1, posicion2):
        distancia_f = abs(posicion1[0] - posicion2[0])
        distancia_c = abs(posicion1[1] - posicion2[1])
        return distancia_f + distancia_c

    # Logica de persecución
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
    
    def jugar_turno(self, jugador, inteligente = True):
        print(f'--- Turno del {jugador.capitalize()} ---')
        if jugador == 'raton':
            nueva_posicion = self.evaluar_mejor_paso_minimax(jugador) if inteligente else self.mover_raton_al_azar()
            self.posicion_raton = nueva_posicion
        else:
            self.posicion_gato = self.evaluar_mejor_paso_minimax(jugador)
        self.mostrar_tablero()

    def verificar_resultado(self):
        if self.posicion_raton == self.posicion_gato:
            return True
        return False

    def obtener_movimientos_legales(self, posicion):
        movimientos = []
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for cambio in direcciones:
            nueva_f, nueva_c = posicion[0] + cambio[0], posicion[1] + cambio[1]

            if 0 <= nueva_f < self.filas and 0 <= nueva_c < self.columnas:
                movimientos.append((nueva_f, nueva_c))
        return movimientos
    
    def minimax(self, profundidad, es_maximizador, posicion_raton, posicion_gato):
        # Condición de parada
        if profundidad == 0 or posicion_raton == posicion_gato:
            return self.calcular_distancia(posicion_raton, posicion_gato)
        
        if es_maximizador:
            mejor_valor = -float('inf')
            for movimiento in self.obtener_movimientos_legales(posicion_raton):
                valor = self.minimax(profundidad - 1, False, movimiento, posicion_gato)
                mejor_valor = max(mejor_valor, valor)
            return mejor_valor
        else:
            mejor_valor = float('inf')
            for movimiento in self.obtener_movimientos_legales(posicion_gato):
                valor = self.minimax(profundidad - 1, True, posicion_raton, movimiento)
                mejor_valor = min(mejor_valor, valor)
            return mejor_valor
    
    def evaluar_mejor_paso_minimax(self, jugador, profundidad = 3):
        movimientos = self.obtener_movimientos_legales(self.posicion_raton if jugador == 'raton' else self.posicion_gato)
        random.shuffle(movimientos)
        mejor_movimiento = movimientos[0]

        if jugador == 'raton':
            mejor_valor = -float('inf')
            for movimiento in movimientos:
                valor_futuro = self.minimax(profundidad, False, movimiento, self.posicion_gato)
                if valor_futuro > mejor_valor:
                    mejor_valor = valor_futuro
                    mejor_movimiento = movimiento
        else:
            mejor_valor = float('inf')
            for movimiento in movimientos:
                valor_futuro = self.minimax(profundidad, True, self.posicion_raton, movimiento)
                if valor_futuro < mejor_valor:
                    mejor_valor = valor_futuro
                    mejor_movimiento = movimiento
        return mejor_movimiento
    
juego = Laberinto(5, 10)

# Bucle de turnos
for i in range(81):
    es_inteligente = i >= 31
    fase = "RATÓN MODO LOCO" if not es_inteligente else "MODO INTELIGENTE"
    print(f'\n--- [{fase}] Turno {i+1 if i < 31 else i-30} ---')
    # Turno del Ratón
    if es_inteligente:
        input('Presiona Enter para que se mueva el RATÓN 🐭 ...')
    juego.jugar_turno('raton', inteligente = es_inteligente)
    if juego.verificar_resultado():
        print('💀¡EL RATÓN FUE ATRAPADO! Fin del juego.')
        break
    # Turno del Gato    
    if es_inteligente:        
        input ('Presiona Enter para que se mueva el GATO 😾 ...')
        juego.jugar_turno('gato')
        if juego.verificar_resultado():
            print('¡EL GATO HA CAZADO! Fin del juego.')
            break
else:
    print('\n🏆 ¡EL RATÓN HA ESCAPADO! El gato se cansó.')