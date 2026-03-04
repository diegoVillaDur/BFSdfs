laberinto = [
    ["S", 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, "G"],
]

# Dimensiones del laberinto
filas = len(laberinto)
columnas = len(laberinto[0])

# Movimientos posibles: arriba, abajo, izquierda, derecha
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
