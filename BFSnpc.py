from collections import deque


def bfs(mapa, inicio, objetivo):
    filas = len(mapa)
    columnas = len(mapa[0])
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    cola = deque()
    cola.append((inicio, [inicio]))  # (estado, camino)

    visitados = set()
    visitados.add(inicio)

    while cola:
        (x, y), camino = cola.popleft()

        if (x, y) == objetivo:
            return camino

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy

            if 0 <= nx < filas and 0 <= ny < columnas:
                if mapa[nx][ny] != 1 and (nx, ny) not in visitados:
                    visitados.add((nx, ny))
                    cola.append(((nx, ny), camino + [(nx, ny)]))

    return None
