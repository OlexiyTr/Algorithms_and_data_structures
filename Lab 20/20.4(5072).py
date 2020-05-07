class Graph:
    def __init__(self, adjacency_matrix):
        self.mAdjacentMatrix = adjacency_matrix

    def GetEdges(self):
        vertices = []
        n = len(self.mAdjacentMatrix)
        for i in range(n):
            neighbors = []
            for j in range(i + 1, n):
                if self.mAdjacentMatrix[i][j] == 1:
                    neighbors.append(j)
            vertices.append(neighbors)
        return vertices

    def GetCount(self):
        count = 0
        n = len(self.mAdjacentMatrix)
        for i in range(n):
            for j in range(n):
                if self.mAdjacentMatrix[i][j] == 1:
                    count += 1
        return count

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
print(graph.GetCount())
