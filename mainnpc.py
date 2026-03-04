import time
from DFSnpc import *
from BFSnpc import *


print("inicio", encontrar_posicion("s"))
print("Meta", encontrar_posicion(2))


# --------------Buscar por BFS
if bfs():
    print("Camino encontrado por BFS:")
    for paso in bfs():
        print(paso)
    print(f"\nLongitud del camino: {len(bfs()) - 1} pasos")


else:
    print("No se encontró un camino.")


# --------------Buscar por DFS
print("Camino encontrado por DFS:")

t_inicio = time.perf_counter()
camino_encontrado = dfs(laberinto, encontrar_posicion("s"), encontrar_posicion(2))
t_fin = time.perf_counter()

print(camino_encontrado)
print(f"\nLongitud del camino: {len(camino_encontrado) - 1} pasos")
print("\nTiempo:", t_fin - t_inicio)
