class Graph:
    def __init__(self, adjacency_matrix):
        self.mVertexNumber = len(adjacency_matrix)

        self.mAdjacentMatrix = adjacency_matrix

    def getPower(self):
        ans = ''
        for i in range(self.mVertexNumber):
            ans += str(sum(self.mAdjacentMatrix[i])) + ' '
        return ans

    def __str__(self):
        s = ''
        for vertex in self.mAdjacentMatrix:
            s = s + str(vertex) + '\n'
        return s

n = int(input())
adjacency_matrix = []
for _ in range(n):
    adjacency_matrix.append(list(map(int, input().split())))
graph = Graph(adjacency_matrix)
print(graph.getPower())
