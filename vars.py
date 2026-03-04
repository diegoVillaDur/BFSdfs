laberinto = [
    ["s", 0, 0, 0, 1],  # Fila 0
    [1, 0, 1, 0, 1],  # Fila 1
    [0, 0, 0, 0, 0],  # Fila 2
    [0, 1, 1, 0, 1],  # Fila 3
    [0, 0, 0, 2, 0],  # Fila 4 (el 2 es el jugador)
]

# Dimensiones del laberinto
filas = len(laberinto)
columnas = len(laberinto[0])

# Movimientos posibles: arriba, abajo, izquierda, derecha
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
