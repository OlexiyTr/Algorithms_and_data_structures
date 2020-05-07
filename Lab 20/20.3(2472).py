class Vertex:
    def __init__(self, vNum):
        self.mVertices = {}
        for i in range(vNum):
            self.mVertices[i+1] = list()

    def AddEdge(self, u, v):
        self.mVertices[u].append(v)
        self.mVertices[v].append(u)

    def neighbors(self, u):
        return [neighbour for neighbour in self.mVertices[u]]

n = int(input())
graph = Vertex(n)
k = int(input())
for _ in range(k):
    st = input().split()
    if st[0] == '1':
        graph.AddEdge(int(st[1]), int(st[2]))
    elif st[0] == '2':
        print(*graph.neighbors(int(st[1])))
