import heapq

def prim(graph, start):
    mst = []
    visited = set()
    edges = [(0, start, start)]

    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))

            for next_v, w in graph[v].items():
                if next_v not in visited:
                    heapq.heappush(edges, (w, v, next_v))
    return mst
