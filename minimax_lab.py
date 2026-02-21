"""
Módulo del Laberinto del Gato y el Ratón

Simulación de persecusión en un tablero bidimensional utilizando
el algoritmo Minimax para la toma de decisiones.

Autor: Carlos Daniel Meza Herrera
Proyecto: Simulación de IA - Minimax
"""
import random

class Laberinto:
    """
    Representa el entorno de simulación y gestiona el estado del juego.

    Esta clase es responsable de mantener la integridad del tablero, 
    validar los movimientos de los agentes (Gato y Ratón) y determinar 
    las condiciones de victoria o derrota.

    Atributos:
        filas (int): Cantidad vertical de celdas en el tablero.
        columnas (int): Cantidad horizontal de celdas en el tablero.
        posicion_raton (tuple): Coordenadas (fila, columna) actuales del agente evasor.
        posicion_gato (tuple): Coordenadas (fila, columna) actuales del agente perseguidor.
        tablero (list): Matriz bidimensional que representa visualmente el estado actual.
    """
    def __init__(self, filas = 5, columnas = 10):
        self.filas = filas
        self.columnas = columnas
        self.posicion_raton = (0, 0)
        self.posicion_gato = (filas - 1, columnas - 1)
        self.tablero = [['.' for _ in range(columnas)] for _ in range(filas)]
    
    def jugar_turno(self, jugador, inteligente = True):
        """
        Ejecuta la lógica de movimiento y actualiza el estado del tablero para un turno específico.

        Este método gestiona la selección de movimiento del agente activo y
        actualiza su posición en el sistema.

        Args:
            jugador (str): Identificador del agente activo ('raton' o 'gato')
            inteligente (bool): Define la estrategia de movimiento.
                Si es True, utiliza el algoritmo Minimax.
                Si es False, utiliza un movimiento aleatorio. Por defecto es True.
        """
        print(f'--- Turno del {jugador.capitalize()} ---')
        if jugador == 'raton':
            nueva_posicion = self.evaluar_mejor_paso_minimax(jugador) if inteligente else self.mover_raton_al_azar()
            self.posicion_raton = nueva_posicion
        else:
            self.posicion_gato = self.evaluar_mejor_paso_minimax(jugador)
        self.mostrar_tablero()
    
    def mostrar_tablero(self):
        """
        Renderiza una representación visual del estado actual del juego.

        Proyecta la matriz del tablero junto con las posiciones actuales
        de los agentes utilizando iconos representativos.
        """
        for fila in range(self.filas):
            for columna in range(self.columnas):
                
                if (fila, columna) == self.posicion_raton:
                    print("🐭", end = " ")
                elif (fila, columna) == self.posicion_gato:
                    print("😾", end = " ")
                else:
                    print(self.tablero[fila][columna], end = " ")
            print()
    
    def verificar_resultado(self):
        """
        Evalúa si el juego ha alcanzado un estado terminal por captura.

        Realiza una detección de colisión entre las coordenadas del
        agente perseguidor y el agente evasor.

        Returns:
            bool: True si el gato ha capturado al ratón (colisión detectada),
                  False si los agentes permanecen en posiciones distintas.
        """
        if self.posicion_raton == self.posicion_gato:
            return True
        return False
    
    # Lógica de persecución minimax
    def evaluar_mejor_paso_minimax(self, jugador, profundidad = 3):
        """
        Determina el movimiento óptimo para el agente actual iniciando el algoritmo Minimax.

        Actúa como la función conductora (driver) que evalúa todas las jugadas legales
        inmediatas y selecciona la que ofrece la mejor puntuación heurística futura.
        
        Args:
            jugador (str): Identificador del agente que debe moverse ('ratón' o 'gato').
            profundidad (int, opcional): Número de niveles (turnos) a simular en el árbol de juego.
        Returns:
            tuple: Coordenadas (fila, columna) correspondiente al mejor movimiento calculado.
        """
        # Obtenemos opciones válidas desde la posición ACTUAL REAL
        movimientos = self.obtener_movimientos_legales(self.posicion_raton if jugador == 'raton' else self.posicion_gato)

        # Mezclamos para evitar que la IA sea predecible en empates
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
    
    def minimax(self, profundidad, es_maximizador, posicion_raton, posicion_gato):
        """
        Núcleo de la IA.
        Evalúa el estado del tablero mediante simulación recursiva de movimientos futuros.

        Args:
            profundidad (int): Número de niveles (turnos) restuantes en el árbol de decisiones.
            es_maximizador (bool): True si es el turno del ratón (maximiza distancia),
                                   False si es el turno del gato (minimiza distancia).
            posicion_raton (tuple): Coordenadas actuales del agente evasor en la simulación.
            posicion_gato (tuple): Coordenadas actuales del agente perseguidor en la simulación.
        Returns:
            int | float: El valor heurístico (distancia Manhattan en enteros) 
                         o infinito (float) calculado para esta rama del árbol.
        """
        # CASO BASE: Condición de parada
        if profundidad == 0 or posicion_raton == posicion_gato:
            return self.calcular_distancia(posicion_raton, posicion_gato)
        
        # Turno del Ratón (Busca MAXimizar distancia)
        if es_maximizador:
            mejor_valor = -float('inf')
            # Probamos todos los movimientos posibles desde la posición imaginaria
            for movimiento in self.obtener_movimientos_legales(posicion_raton):
                valor = self.minimax(profundidad - 1, False, movimiento, posicion_gato)
                mejor_valor = max(mejor_valor, valor)
            return mejor_valor
        
        # Turno del Gato (Busca MINimizar distancia)
        else:
            mejor_valor = float('inf')
            for movimiento in self.obtener_movimientos_legales(posicion_gato):
                valor = self.minimax(profundidad - 1, True, posicion_raton, movimiento)
                mejor_valor = min(mejor_valor, valor)
            return mejor_valor
    
    # MÉTODO LEGADO: Lógica de persecución básica (Búsqueda codiciosa)
    def evaluar_mejor_paso(self, jugador):
        """
        Calcula el siguiente paso evaluando solo la heurística inmediata (Greedy Search).

        ¡ADVERTENCIA! Método Deprecado (Obsoleto).
        Este método tomaba decisiones miopes mirando solo un turno a la vez.
        Ha sido reemplazado por 'evaluar_mejor_paso_minimax' para habilitar
        el análisis de profundidad. Se conserva para pruebas comparativas.

        Args:
            jugador (str): Identificador del agente ('raton' o 'gato')
        Returns:
            tuple: Coordenadas (fila, columna) del movimiento inmediato seleccionado
        """
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
    
    def obtener_movimientos_legales(self, posicion):
        """
        Calcula las celdas adyacentes válidas desde una posición específica.

        Evalúa los límites del tablero para garantizar que los agentes no
        salgan de la matriz permitida.

        Args:
            posicion (tuple): Coordenadas actuales (fila, columna) a evaluar.       
        Returns:
            list: Lista de tuplas con las coordenadas de los movimientos legales.
        """
        movimientos = []
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for cambio in direcciones:
            nueva_f, nueva_c = posicion[0] + cambio[0], posicion[1] + cambio[1]

            if 0 <= nueva_f < self.filas and 0 <= nueva_c < self.columnas:
                movimientos.append((nueva_f, nueva_c))
        return movimientos
    
    def calcular_distancia(self, posicion1, posicion2):
        """
        Calcula la Heurística de distancia Manhattan entre dos puntos.

        Args:
            posicion1 (tuple): Coordenadas (fila, columna) del punto A.
            posicion2 (tuple): Coordenadas (fila, columna) del punto B.
        Returns:
            int: La distancia en bloques ortogonales (sin diagonales) entre los puntos.
        """
        distancia_f = abs(posicion1[0] - posicion2[0])
        distancia_c = abs(posicion1[1] - posicion2[1])
        return distancia_f + distancia_c
    
    def mover_raton_al_azar(self):
        """
        Selecciona y ejecuta un movimiento aleatorio válido para el ratón.

        Returns:
            tuple: Las nuevas coordenadas (fila, columna) tras el movimiento.
        """
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        cambio = random.choice(direcciones) # Aleatoriedad de direcciones

        nueva_f = self.posicion_raton[0] + cambio[0]
        nueva_c = self.posicion_raton[1] + cambio[1]

        # Validar posición para que no salga del tablero
        if 0 <= nueva_f < self.filas and 0 <= nueva_c < self.columnas:
            return (nueva_f, nueva_c)
        return self.posicion_raton

juego = Laberinto(5, 10)

# --- BUCLE PRINCIPAL DEL JUEGO (GAME LOOP) ---
# Este bloque actúa como el "Director de Orquesta", coordinando los turnos
# y el flujo de la simulación hasta alcanzar un estado de parada.

for i in range(81):
    # El ratón inicia en "Modo Loco" (azar) para simular un periodo de
    # desorientación antes de activar su IA de escape a partir del turno 31.
    es_inteligente = i >= 31
    fase = "RATÓN MODO LOCO" if not es_inteligente else "MODO INTELIGENTE"
    print(f'\n--- [{fase}] Turno {i+1 if i < 31 else i-30} ---')

    # Gestión del turno del Ratón (Agente Evasor)
    if es_inteligente:
        input('Presiona Enter para que se mueva el RATÓN 🐭 ...')       
    juego.jugar_turno('raton', inteligente = es_inteligente)

    # Verificación de captura inmediata tras el movimiento del ratón
    if juego.verificar_resultado():
        print('💀¡EL RATÓN FUE ATRAPADO! Fin del juego.')
        break

    # Gestión del turno del Gato (Agente Perseguidor)    
    if es_inteligente:        
        input ('Presiona Enter para que se mueva el GATO 😾 ...')
        juego.jugar_turno('gato')

        # El juego termina si el gato alcanza la posición del ratón en su turno
        if juego.verificar_resultado():
            print('¡EL GATO HA CAZADO! Fin del juego.')
            break
else:
    # Condición de escape: se alcanza el límite de turnos sin captura
    print('\n🏆 ¡EL RATÓN HA ESCAPADO! El gato se cansó.')