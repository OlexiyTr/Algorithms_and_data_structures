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

class Maze:
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def __init__(self, matrix, wall, cell):
        self.mMatrix = matrix
        self.mWall = wall
        self.mCell = cell

    def get_area(self, i, j):
        visited = [[0 for __ in range(len(self.mMatrix))]
                   for _ in range(len(self.mMatrix))]
        visited[i][j] = 1
        count = 0
        q = Queue()
        q.enqueue((i, j))
        while not q.empty():
            i, j = q.dequeue()
            count += 1

            for di, dj in Maze.directions:
                ii, jj = i + di, j + dj
                if (self.mMatrix[ii][jj] == self.mCell and not visited[ii][jj]):
                    q.enqueue((ii, jj))
                    visited[ii][jj] = 1
        return count

di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]

def wave_second(maze, start):
    n = len(maze)
    m = len(maze[0])
    waveMatrix = [[100000] * m for i in range(n)]

    q = Queue()
    q.enqueue(start)
    waveMatrix[start[0]][start[1]] = 0

    while not q.empty():
        current = q.dequeue()
        i, j = current[0], current[1]
        for k in range (len(dj)):
            i1, j1 = i + di[k], j + dj[k]
            if waveMatrix[i1][j1] == 100000 and maze[i1][j1] != 'R' and maze[i1][j1] != 'e':
                q.enqueue((i1, j1))
                waveMatrix[i1][j1] = waveMatrix[i][j] + 1
    return waveMatrix

def wave_first(maze, swave, start):
    n = len(maze)
    m = len(maze[0])
    waveMatrix = [[100000] * m for i in range(n)]

    q = Queue()
    q.enqueue(start)
    waveMatrix[start[0]][start[1]] = 0

    while not q.empty():
        current = q.dequeue()
        i, j = current[0], current[1]
        for k in range (len(dj)):
            i1, j1 = i + di[k], j + dj[k]
            if waveMatrix[i1][j1] == 100000 and maze[i1][j1] != 'R' and waveMatrix[i][j] + 1 < swave[i1][j1]:
                q.enqueue((i1, j1))
                waveMatrix[i1][j1] = waveMatrix[i][j] + 1
    return waveMatrix


start1 = 0
start2 = 0
end = 0

tests = int(input())
for test in range(tests):
    n, m =  map(int, input().split())
    mtr = []
    for i in range(n):
        mtr.append(list(input()))
        if 'g' in mtr[i]:
            start1 = (i,mtr[i].index('g'))
        if 'l' in mtr[i]:
            start2 = (i,mtr[i].index('l'))
        if 'e' in mtr[i]:
            end = (i,mtr[i].index('e'))
    swave = wave_second(mtr, start2)
    #pprint(swave)
    fwawe = wave_first(mtr, swave, start1)
    #pprint(fwawe)
    print('YES' if fwawe[end[0]][end[1]] <= 1000 else 'NO')
