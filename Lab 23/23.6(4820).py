from pprint import pprint

class Node:
    def __init__(self, item):
        self.mItem = item
        self.mNext = None

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

di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]

def CanGo(i, j, n, m):
    if i<0 or i>=n or j<0 or j>=m:
        return False
    return True

def wave(maze, start, end):
    n = len(maze)
    m = len(maze[0])
    waveMatrix = [[-1]*m for i in range(n)]
    #pprint(maze)
    #pprint(waveMatrix)
    q = Queue()
    q.enqueue(start)
    waveMatrix[start[0]][start[1]] = 0
    while not q.empty():
        current = q.dequeue()
        i, j = current[0], current[1]
        for k in range(len(dj)):
            i1, j1 = i + di[k], j + dj[k]
            if CanGo(i1, j1, n, m) and waveMatrix[i1][j1] == -1 and maze[i1][j1] == 0:
                q.enqueue((i1, j1))
                waveMatrix[i1][j1] = waveMatrix[i][j] + 1
                if end[0] == i1 and end[1] == j1:
                    break
    #pprint(waveMatrix)
    return  waveMatrix[end[0]][end[1]] if waveMatrix[end[0]][end[1]] != -1 else -1

start = 0
end = 0

n, m = map(int, input().split())
mtr = []
for i in range(n):
    mtr.append(list(map(int, input().split())))
start = list(map(int, input().split()))
start[0], start[1] = start[1]-1, start[0]-1
end = list(map(int, input().split()))
end[0], end[1] = end[1]-1, end[0]-1

print(wave(mtr, start, end))
