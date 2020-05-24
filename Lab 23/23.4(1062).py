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

def CanGo(i, j, n):
    if i<0 or i>=n or j<0 or j>=n:
        return False
    return True

def wave(maze, start):
    n = len(maze)
    waveMatrix = [[-1] * n for i in range(n)]
    q = Queue()
    q.enqueue(start)
    waveMatrix[start[0]][start[1]] = 0
    while not q.empty():
        current = q.dequeue()
        i, j = current[0], current[1]
        for k in range(len(dj)):
            i1, j1 = i + di[k], j + dj[k]
            if CanGo(i1, j1, n) and waveMatrix[i1][j1] == -1 and maze[i1][j1] != 'O':
                q.enqueue((i1, j1))
                waveMatrix[i1][j1] = waveMatrix[i][j] + 1
    return waveMatrix

def findWay(maze, start, end):
    waveMatrix = wave(maze, start)

    if waveMatrix[end[0]][end[1]] == -1:
        print('N')
        return

    n = len(waveMatrix)
    matrix = maze

    matrix[end[0]][end[1]] = "+"

    current = end
    while True:
        if current == start:
            matrix[current[0]][current[1]] = "@"
            break

        i = current[0]
        j = current[1]

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            current = None
            if CanGo(i1, j1, n) and waveMatrix[i1][j1] == waveMatrix[i][j] - 1:
                current = (i1, j1)
                matrix[i1][j1] = "+"
                break
    print('Y')
    for i in range(len(matrix)):
        print(''.join(matrix[i]))


start = 0
end = 0

n = int(input())
mtr = []
for i in range(n):
    mtr.append(list(input()))
    if '@' in mtr[i]:
        start = (i,mtr[i].index('@'))
    if 'X' in mtr[i]:
        end = (i,mtr[i].index('X'))
findWay(mtr, start, end)
