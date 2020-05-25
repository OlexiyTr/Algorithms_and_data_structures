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

def wave(maze):
    n = len(maze)
    m = len(maze[0])
    waveMatrix = [[-1] * m for i in range(n)]
    count = 1
    for i in range(n):
        for j in range(m):
            if waveMatrix[i][j] == -1 and maze[i][j] == '#':
                q = Queue()
                q.enqueue((i, j))
                waveMatrix[i][j] = count
                while not q.empty():
                    current = q.dequeue()
                    ii, jj = current[0], current[1]
                    for k in range(len(dj)):
                        i1, j1 = ii + di[k], jj + dj[k]
                        if CanGo(i1, j1, n, m) and waveMatrix[i1][j1] == -1 and maze[i1][j1] == '#':
                            q.enqueue((i1, j1))
                            waveMatrix[i1][j1] = count
                count += 1
    #pprint(waveMatrix)
    return count

n, m = map(int, input().split())
mtr = []
for i in range(n):
    mtr.append(list(input()))
print(wave(mtr)-1)
