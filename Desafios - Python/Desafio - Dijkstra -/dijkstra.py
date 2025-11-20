import numpy as np

grafo = np.array([
    [0,   10,  0,  30, 100],
    [10,   0, 50,   0,   0],
    [0,   50,  0,  20,  10],
    [30,   0, 20,   0,  60],
    [100,  0, 10,  60,   0]
])

def dijkstra(grafo, inicio):
    n = len(grafo)
    dist = [float('inf')] * n #[float('inf')] é um valor infinito
    visitado = [False] * n
    dist[inicio] = 0

    for _ in range(n):
        menor = float('inf')
        u = -1

        # Escolhe o nó não visitado com menor distância
        for i in range(n):
            if not visitado[i] and dist[i] < menor:
                menor = dist[i]
                u = i

        visitado[u] = True

        # Atualiza as distâncias dos vizinhos
        for v in range(n):
            if grafo[u][v] > 0 and not visitado[v]:
                nova_dist = dist[u] + grafo[u][v]
                if nova_dist < dist[v]:
                    dist[v] = nova_dist

    return dist


resultado = dijkstra(grafo, 0) #Executa o dijkstra a partir do nó 0

print("Menores distâncias a partir do nó 0:")

for i, d in enumerate(resultado):
    print(f"De 0 até {i} = {d}")