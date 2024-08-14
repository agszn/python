class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for adjacent in self.graph[vertex]:
                self.graph[adjacent].remove(vertex)
            del self.graph[vertex]

    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")

# Example usage
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_edge("A", "B")
g.print_graph()  # A: ['B'] \n B: ['A']
g.remove_edge("A", "B")
g.print_graph()  # A: [] \n B: []
