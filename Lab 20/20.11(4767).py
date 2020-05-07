class Graph:
    def __init__(self, oriented=False, vertex_number=20):
        self.mIsOriented = oriented
        self.mVertexNumber = vertex_number

        self.mAdjacentMatrix = []
        for i in range(self.mVertexNumber):
            self.mAdjacentMatrix.append([0] * self.mVertexNumber)

    def addEdge(self, source, destination, weight=1):
        self.mAdjacentMatrix[source][destination] = weight

        if not self.mIsOriented:
            self.mAdjacentMatrix[destination][source] = weight

    def __str__(self):
        matrix = ''
        for i in range(self.mVertexNumber):
            matrix += '\n'
            for j in range(self.mVertexNumber):
                matrix += str(self.mAdjacentMatrix[i][j]) + ' '
        return matrix

n, k = map(int, input().split())
graph = Graph(True, n)
for _ in range(k):
    u, v = map(int, input().split())
    graph.addEdge(u-1, v-1)
print(graph)
