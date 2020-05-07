class Graph:
    def __init__(self, oriented=False, vertex_number=20):
        self.mIsOriented = oriented
        self.mVertexNumber = vertex_number

        self.mAdjacentMatrix = []
        for i in range(self.mVertexNumber):
            self.mAdjacentMatrix.append([0] * self.mVertexNumber)

    def addEdge(self, source, destination, weight=1):
        self.mAdjacentMatrix[source][destination] += weight
        if self.mAdjacentMatrix[source][destination] > 1:
            print('YES')
            exit(0)

        if not self.mIsOriented:
            self.mAdjacentMatrix[destination][source] = weight

    def __str__(self):
        s = ''
        for vertex in self.mAdjacentMatrix:
            s = s + str(vertex) + '\n'
        return s

n, k = map(int, input().split())
graph = Graph(True, n)
for _ in range(k):
    u, v = map(int, input().split())
    graph.addEdge(u-1, v-1)

print('NO')
