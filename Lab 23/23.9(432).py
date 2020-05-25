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

di = [0, 0, -1, 0, 0, 1]
dj = [0, -1, 0, 0, 1, 0]
dk = [-1, 0, 0, 1, 0, 0]

def CanGo(i, j, k, n, m ,l):
    if i<0 or i>=n or j<0 or j>=m or k<0 or k>=l:
        return False
    return True

def wave(maze, start, end):
    n = len(maze)
    m = len(maze[0])
    l = len(maze[0][0])
    waveMatrix = [[[-1]*l for __ in range(m)] for _ in range(n)]
    #pprint(maze)
    #pprint(waveMatrix)
    q = Queue()
    q.enqueue((start[0],start[1],start[2]))
    waveMatrix[start[0]][start[1]][start[2]] = 0
    while not q.empty():
        current = q.dequeue()
        i, j, k = current[0], current[1], current[2]
        for s in range(len(dj)):
            i1, j1, k1 = i + di[s], j + dj[s], k + dk[s]
            if CanGo(i1, j1, k1, n, m ,l) and waveMatrix[i1][j1][k1] == -1 and maze[i1][j1][k1] != '#':

                q.enqueue((i1, j1, k1))
                waveMatrix[i1][j1][k1] = waveMatrix[i][j][k] + 1
    #pprint(waveMatrix)
    return  waveMatrix[end[0]][end[1]][end[2]]

start = 0
end = 0

x1, x2, x3 = map(int, input().split())
while (x1+x2+x3 != 0):
    mtr = []
    for i in range(x1):
        mtr.append([])
        for j in range(x2):
            mtr[i].append(list(input()))
            if 'S' in mtr[i][j]:
                start = (i,j,mtr[i][j].index('S'))
            if 'E' in mtr[i][j]:
                end = (i,j,mtr[i][j].index('E'))
        input()
    x = wave(mtr, start, end)
    print('Trapped!' if x == -1 else f'Escaped in {x} minute(s).')
    x1, x2, x3 = map(int, input().split())
    #pprint(mtr)
