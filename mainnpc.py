import time
from DFSnpc import *
from BFSnpc import *


print("\ninicio", encontrar_posicion("s"))
print("Meta", encontrar_posicion(2), "\n")


# --------------Buscar por BFS
t_inicio = time.perf_counter()
if bfs():
    print("Camino encontrado por BFS:")
    for paso in bfs():
        print(paso)
    print(f"Meta encontrada\nLongitud del camino: {len(bfs()) - 1} pasos")
else:
    print("No se encontró un camino.")
t_fin = time.perf_counter()
print("Tiempo:", t_fin - t_inicio)

# --------------Buscar por DFS
print("\nCamino encontrado por DFS:")

t_inicio = time.perf_counter()
camino_encontrado = dfs(laberinto, encontrar_posicion("s"), encontrar_posicion(2))
t_fin = time.perf_counter()

print(f"Longitud del camino: {len(camino_encontrado) - 1} pasos")
print("Tiempo:", t_fin - t_inicio)
