class Graph:
    def __init__(self, adjacency_matrix):
        self.mVertexNumber = len(adjacency_matrix)

        self.mAdjacentMatrix = adjacency_matrix

    def getPower(self):
        ans = ''
        for i in range(self.mVertexNumber):
            for j in range(self.mVertexNumber):
                if self.mAdjacentMatrix[i][j] != 0:
                    print(f'{i+1} {j+1}')

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
graph.getPower()
