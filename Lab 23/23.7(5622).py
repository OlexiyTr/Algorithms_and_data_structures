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

def wave(maze, waveMatrix, start, count):
    n = len(maze)
    print('aa')
    #pprint(maze)
    #pprint(waveMatrix)
    q = Queue()
    q.enqueue((start[0],start[1]))
    waveMatrix[start[0]][start[1]] = 1
    while not q.empty():
        current = q.dequeue()
        i, j = current[0], current[1]
        for k in range(len(dj)):
            i1, j1 = i + di[k], j + dj[k]
            if CanGo(i1, j1, n) and waveMatrix[i1][j1] == -1 and maze[i1][j1] == '.':
                q.enqueue((i1, j1))
                waveMatrix[i1][j1] = 1
            elif not CanGo(i1, j1, n) or maze[i1][j1] == '#':
                #print(i1,j1)
                count[0] += 1
    #pprint(waveMatrix)
    return  count

start = 0
end = 0

n = int(input())
mtr = []
for i in range(n):
    mtr.append(list(input()))

count = [0]
waveMatrix = [[-1]*n for i in range(n)]
wave(mtr, waveMatrix, (0,0), count)
#pprint(waveMatrix)
if waveMatrix[n-1][n-1] == -1:
    wave(mtr, waveMatrix,(n-1,n-1), count)
#pprint(waveMatrix)

print((count[0]-4)*9)
