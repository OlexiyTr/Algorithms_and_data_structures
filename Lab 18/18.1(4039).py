class Heap:

    def __init__(self):
        self.mItems = [0]
        self.mSize = 0

    def __len__(self):
        return self.mSize

    def empty(self):
        return len(self.mItems) == 1

    def insert(self, *k):
        self.mSize += 1
        self.mItems.append(k[0])
        self.siftUp()

    def extractMax(self):
        if not self.empty():
            root = self.mItems[1]
            self.mItems[1] = self.mItems[-1]
            self.mItems.pop()
            self.mSize -= 1
            self.siftDown()
            return root

    def siftDown(self):
        i = 1
        while (2 * i) <= self.mSize:
            left = 2 * i
            right = 2 * i + 1
            min_child = self.maxChild(left, right)
            if self.mItems[i] < self.mItems[min_child]:
                self.swap(min_child, i)
            i = min_child

    def siftUp(self):
        i = len(self.mItems) - 1
        while i > 1:
            parent = i // 2
            if self.mItems[i] > self.mItems[parent]:
                self.swap(parent, i)
            i = parent

    def swap(self, i, j):
        self.mItems[i], self.mItems[j] = self.mItems[j], self.mItems[i]

    def maxChild(self, left_child, right_child):
        if right_child > self.mSize:
            return left_child
        else:
            if self.mItems[left_child] > self.mItems[right_child]:
                return left_child
            else:
                return right_child

heap = Heap()
n = int(input())

for i in range(n):
    st = input().split()
    if st[0] == '0':
        heap.insert(int(st[1]))
    elif st[0] == '1':
        print(heap.extractMax())
