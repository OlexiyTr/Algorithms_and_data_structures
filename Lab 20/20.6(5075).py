class Vertex:
    def __init__(self, vNum):
        self.mVertices = {}
        self.mSize = vNum
        for i in range(vNum):
            self.mVertices[i+1] = [[],[]]

    def AddEdge(self, u, v):
        self.mVertices[u][0].append(v)
        self.mVertices[v][1].append(u)

    def neighbors(self):
        for i in range(self.mSize):
            print(len(self.mVertices[i+1][1]), len(self.mVertices[i+1][0]))



n, k = map(int, input().split())
graph = Vertex(n)
for _ in range(k):
    u, v = map(int, input().split())
    graph.AddEdge(u, v)

graph.neighbors()
