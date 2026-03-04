from vars import *

def dfs(laberinto, inicio, meta):
    # Implementación didáctica del algoritmo DFS
    # Pila (LIFO)
    pila = [(inicio, [inicio])]
    visitados = set()

    while pila:
        (x, y), camino = pila.pop()

        if (x, y) in visitados:
            continue

        visitados.add((x, y))

        print(f"{(x, y)}")
        if (x, y) == meta:
            print("Meta encontrada")
            return camino

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy

            if (
                0 <= nx < len(laberinto)
                and 0 <= ny < len(laberinto[0])
                and laberinto[nx][ny] != 1
                and (nx, ny) not in visitados
            ):
                pila.append(((nx, ny), camino + [(nx, ny)]))
    return None
