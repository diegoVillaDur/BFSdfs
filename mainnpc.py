from DFSnpc import *
from BFSnpc import *


camino_encontrado = bfs()

# Mostramos resultados
if camino_encontrado:
    print("Camino encontrado por BFS:")
    for paso in camino_encontrado:
        print(paso)
    print(f"\nLongitud del camino: {len(camino_encontrado) - 1} pasos")
else:
    print("No se encontró un camino.")
