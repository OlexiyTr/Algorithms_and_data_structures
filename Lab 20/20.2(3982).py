class Vertex:
    def __init__(self):
        self.mVertices = {}

    def AddEdge(self, i, j):
        self.mVertices[i] = j

    def __str__(self):
        matrix = ''
        for i in range(1, len(self.mVertices) + 1):
            matrix += '\n'
            for j in range(1, len(self.mVertices) + 1):
                x = 1 if (j in self.mVertices[i]) else 0
                matrix += str(x) + ' '
        return matrix

n = int(input())
graph = Vertex()
for i in range(n):
    edges = tuple(map(int, input().split()))[1:]
    graph.AddEdge(i+1, set(edges))
print(graph)
