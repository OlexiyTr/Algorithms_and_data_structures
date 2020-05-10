class Node:
    def __init__(self, item):
        self.mItem = item
        self.mNext = None


class Stack:

    def __init__(self):
        self.mTopNode = None

    def empty(self) -> bool:
        return self.mTopNode is None

    def push(self, item):
        new_node = Node(item)
        if not self.empty():
            new_node.mNext = self.mTopNode
        self.mTopNode = new_node

    def pop(self):
        if self.empty():
            raise Exception("Stack: 'pop' applied to empty container")

        current_top = self.mTopNode
        item = current_top.mItem
        self.mTopNode = self.mTopNode.mNext
        del current_top

        return item

    def top(self):
        if self.empty():
            raise Exception("Stack: 'top' applied to empty container")
        return self.mTopNode.mItem

class Queue:

    def __init__(self):
        self.mFront = None
        self.mBack = None

    def empty(self):
        return self.mFront is None and self.mBack is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.empty():
            self.mFront = new_node
        else:
            self.mBack.mNext = new_node

        self.mBack = new_node

    def dequeue(self):
        if self.empty():
            raise Exception("Queue: 'dequeue' applied to empty container")

        current_front = self.mFront
        item = current_front.mItem
        self.mFront = self.mFront.mNext
        del current_front

        if self.mFront is None:
            self.mBack = None
        return item

class VertexBase:

    def __init__(self, key):
        self.mKey = key
        self.mData = None

    def key(self): return self.mKey
    def setData(self, data): self.mData = data
    def data(self): return self.mData
    def __str__(self): return str(self.mKey) + ": Data=" + str(self.data())

class Vertex(VertexBase):

    def __init__(self, key):
        super().__init__(key)
        self.mNeighbors = {}

    def addNeighbor(self, vertex, weight=1):
        if isinstance(vertex, VertexBase):
            self.mNeighbors[vertex.key()] = weight
        else:
            self.mNeighbors[vertex] = weight

    def neighbors(self):
        return self.mNeighbors.keys()

    def weight(self, neighbor):
        if isinstance(neighbor, VertexBase):
            return self.mNeighbors[neighbor.key()]
        else:
            return self.mNeighbors[neighbor]

    def __str__(self):
        return super().__str__() + ' connected to: ' + str(self.mNeighbors)

class Graph:

    def __init__(self, oriented=False):
        self.mIsOriented = oriented
        self.mVertexNumber = 0
        self.mVertices = {}

    def addVertex(self, vertex):
        if vertex in self:
            return False
        new_vertex = Vertex(vertex)
        self.mVertices[vertex] = new_vertex
        self.mVertexNumber += 1
        return True

    def getVertex(self, vertex):
        assert vertex in self
        key = vertex.key() if isinstance(vertex, Vertex) else vertex
        return self.mVertices[key]

    def vertices(self):
        return self.mVertices

    def addEdge(self, source, destination, weight=1):
        if source not in self:
            self.addVertex(source)
        if destination not in self:
            self.addVertex(destination)
        self[source].addNeighbor(destination, weight)
        if not self.mIsOriented:
            self.mVertices[destination].addNeighbor(source, weight)

    def setData(self, vertex, data):
        assert vertex in self
        self[vertex].setData(data)

    def getData(self, vertex):
        assert vertex in self
        return self[vertex].data()

    def transpose(self):
        g_inv = Graph(self.mIsOriented)
        for vertex in self:
            for neighbor_key in vertex.neighbors():
                g_inv.addEdge(neighbor_key, vertex.key())

        return g_inv

    def __contains__(self, vertex):
        if isinstance(vertex, Vertex):
            return vertex.key() in self.mVertices
        else:
            return vertex in self.mVertices

    def __iter__(self):
        return iter(self.mVertices.values())

    def __len__(self):
        return self.mVertexNumber

    def __str__(self):
        s = ""
        for vertex in self:
            s = s + str(vertex) + "\n"
        return s

    def __getitem__(self, vertex):
        return self.getVertex(vertex)

def __dfs_helper(graph, visited, recVisited, start):
    visited.add(start)
    recVisited.add(start)
    for neighbour in graph[start].neighbors():
        if neighbour not in visited:
            if __dfs_helper(graph, visited, recVisited, neighbour) == True:
                return True
        elif neighbour in recVisited:
            return True
    recVisited.discard(start)
    return False

def isCyclic(graph):
    visited = set()
    recVisited = set()
    for node in graph:
        if node not in visited:
            if __dfs_helper(graph, visited, recVisited, node.key()) == True:
                return True
    return False

n = int(input())
mtr = []
for i in range(n):
    mtr.append(list(map(int, input().split())))
graph = Graph(True)

for i in range(n):
    for j in range(n):
        if mtr[i][j] == 1:
            graph.addEdge(i+1, j+1)

try:
    if isCyclic(graph):
        print(1)
    else:
        print(0)
except:
    print(0)
