from collections import deque
from encontrar import *


def bfs():
    """
    Implementación del algoritmo BFS
    """
    inicio = encontrar_posicion("S")
    meta = encontrar_posicion("G")

    # Cola para BFS: almacena (posición, camino recorrido)
    cola = deque()  # Crea una cola vacía donde se guardarán los estados por explorar.
    cola.append((inicio, [inicio]))

    # Conjunto de estados visitados
    visitados = set()
    visitados.add(inicio)

    while cola:
        (x, y), camino = cola.popleft()
        """Se saca el primer elemento de la cola
        coordenadas actuales del agente en el laberinto"""

        # Si llega a la meta, regresamos el camino
        if (x, y) == meta:
            return camino

        # Exploramos vecinos
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy

            # Verificamos límites del laberinto
            if 0 <= nx < filas and 0 <= ny < columnas:
                # Verificamos que no sea pared y no esté visitado
                if laberinto[nx][ny] != 1 and (nx, ny) not in visitados:
                    visitados.add((nx, ny))
                    cola.append(((nx, ny), camino + [(nx, ny)]))
        """
        x, y → donde estás
        (dx, dy) → “un paso”
        nx, ny → a dónde llegas si das ese paso"""

    # Si no hay solución
    return None
