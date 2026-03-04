from vars import *


def encontrar_posicion(elemento):
    # Busca la posición del elemento en el laberinto
    for i in range(filas):
        for j in range(columnas):
            if laberinto[i][j] == elemento:
                return (i, j)
    return None
