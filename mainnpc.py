from DFSnpc import dfs
from BFSnpc import bfs

mapa = [
    [0, 0, 0, 0, 1],  # Fila 0
    [1, 0, 1, 0, 1],  # Fila 1
    [0, 0, 2, 0, 0],  # Fila 2
    [0, 1, 1, 0, 1],  # Fila 3
    [0, 0, 0, 0, 2],  # Fila 4 (el 2 es el jugador)
]

# Dimensiones del mapa
filas = len(mapa)
columnas = len(mapa[0])

# Movimientos posibles: arriba, abajo, izquierda, derecha
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

inicio = (0, 0)
objetivo = (4, 4)  # o puedes buscar automáticamente el '2'


camino_bfs = bfs(mapa, inicio, objetivo)
camino_dfs = dfs(mapa, inicio, objetivo)

print("BFS:", camino_bfs)
print("DFS:", camino_dfs)
