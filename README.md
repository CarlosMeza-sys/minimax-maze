# Simulador Minimax en Python

Este proyecto es una simulación de persecución desarrollada en Python puro, donde dos agentes de Inteligencia Artificial (un Gato y un Ratón) se enfrentan en un tablero bidimensional. 

Ambos agentes son controlados por el mismo motor lógico central, pero lo utilizan para fines completamente opuestos: el gato persigue al ratón intentando acorralarlo, mientras que el ratón evalúa las rutas para huir y mantenerse a salvo.

Para lograr esto, cada agente realiza una simulación antes de moverse: evalúa sus pasos posibles, "se pone en los zapatos" de su enemigo para predecir cuál será su mejor respuesta, y proyecta este intercambio hasta una profundidad de 3 capas. En base a ese futuro simulado, toman su decisión final en el presente.

### 📜 Dinámica y Reglas del Juego

La partida tiene un límite de tiempo estructurado en dos fases:
* **Fase 1 - Desorientación (Turnos 1 al 30):** El ratón se mueve de forma totalmente aleatoria por el tablero, mientras el gato espera.
* **Fase 2 - Cacería Inteligente (Turnos 31 al 80):** Se activa el algoritmo Minimax. Durante los siguientes 50 turnos, ambos agentes se mueven de forma calculada y estratégica persiguiendo sus objetivos.

**Condiciones de Victoria:**
* 😾 **Gato:** Gana si logra atrapar al ratón (coincidir en la misma coordenada) antes de que se agoten los turnos.
* 🐭 **Ratón:** Gana si logra evadir al gato y sobrevivir hasta que finalicen los 50 turnos de la fase inteligente.

## 🚀 Instrucciones de Ejecución

Para ver la simulación en acción, los pasos son muy sencillos:

1. Descarga el archivo de Python (`minimax_lab.py`).
2. Abre tu terminal y ejecuta el siguiente script:
``` bash
python minimax_lab.py
```
3. **Fase de Desorientación:** El programa ejecutará automáticamente los primeros 30 turnos, donde verás al ratón moviéndose de forma completamente aleatoria por el tablero.
4. **Fase Inteligente:** A partir del turno 31, la simulación se volverá interactiva. Solo necesitas presionar la tecla `Enter` para avanzar turno a turno. Podrás observar cómo cada agente toma decisiones calculadas hasta que se agoten los 50 turnos de esta fase o el gato logre su captura.

---

## 📓 Bitácora de Aprendizaje (Mis momentos "¡Ajá!")

Este proyecto fue un desafío de lógica pura. A lo largo del desarrollo, me encontré con tres revelaciones técnicas que me hicieron entender cómo "piensa" realmente la máquina:

* **El "Burbujeo" de la Recursividad:** Me costó entender cómo los valores regresaban al origen, hasta que pude visualizar el "burbujeo" (Unwinding). Cuando la simulación llega a la última capa (profundidad 0), deja de imaginar y calcula la distancia real. Ese número exacto comienza a "burbujear" hacia arriba, pasando de la profundidad 1, a la 2 y finalmente a la 3. El caso base detiene la caída y hace que la realidad salga a flote.
* **Empatía Algorítmica (Ponerse en los zapatos del enemigo):** Entender cómo el método `minimax` se llama a sí mismo fue increíble. Pero la verdadera genialidad fue ver que, al llamarse a sí mismo pasándole argumentos invertidos (cambiando el booleano del turno opuesto), la IA literalmente se "pone en los zapatos" de su adversario para simular cuál sería su mejor respuesta antes de tomar una decisión en el presente.
* **La Sintaxis del Infinito:** Descubrir cómo inicializar los peores escenarios posibles. Fue interesante aprender que para arrancar las comparaciones, tenía que invocar al infinito matemático usando un string dentro de una función de números decimales: `float('inf')` y `-float('inf')`. Una herramienta de sintaxis extraña pero poderosísima.

---

## 👨‍💻 Autor

**Carlos Daniel Meza Herrera** | Python Developer | *Apasionado por la Inteligencia Artificial y la Lógica de Software.*