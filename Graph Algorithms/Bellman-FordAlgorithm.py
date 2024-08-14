def bellman_ford(graph, V, E, src):
    dist = [float("Inf")] * V
    dist[src] = 0

    for _ in range(V - 1):
        for u, v, w in graph:
            if dist[u] != float
