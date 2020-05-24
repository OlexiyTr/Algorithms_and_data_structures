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

n = int(input())
mtr = []
for i in range(n):
    mtr.append(list(input()))
i, j = map(int, input().split())
print(Maze(mtr, '*', '.').get_area(i - 1, j - 1))
