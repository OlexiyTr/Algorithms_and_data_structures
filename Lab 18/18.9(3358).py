class PQElement:
    INF = 100000

    def __init__(self, item=None, priority=INF):
        self.mItem = item
        self.mPriority = priority

    def __getitem__(self, item):
        if item == 0:
            return self.mItem
        elif item == 1:
            return self.mPriority
        else:
            raise IndexError

    def __setitem__(self, key, value):
        if key == 0:
            self.mItem = value
        elif key == 1:
            self.mPriority = value
        else:
            raise IndexError

    def setPriority(self, priority): self.mPriority = priority
    def setItem(self, item): self.mItem = item
    def priority(self): return self.mPriority
    def item(self): return self.mItem
    def __str__(self): return "{} {}".format(self.mItem, self.mPriority)
    def __le__(self, other): return self.mPriority <= other.mPriority
    def __lt__(self, other):
        if self.mPriority == other.mPriority:
            return int(self.mItem) > int(other.mItem)
        else:
            return self.mPriority < other.mPriority
    def __gt__(self, other):
        if self.mPriority == other.mPriority:
            return int(self.mItem) < int(other.mItem)
        else:
            return self.mPriority > other.mPriority
    def __ge__(self, other): return self.mPriority >= other.mPriority

class Heap:

    def __init__(self):
        self.mItems = [0]
        self.mSize = 0

    def isRoot(self, i): return i == 1
    def getLeft(self, i): return i * 2
    def getRight(self, i): return i * 2 + 1
    def getParent(self, i): return i // 2

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

class PriorityQueue(Heap):

    def __init__(self):
        super().__init__()
        self.mElementsMap = {}

    def swap(self, i, j):

        pos_i = self.mItems[i].item()
        pos_j = self.mItems[j].item()
        self.mElementsMap[pos_i] = j
        self.mElementsMap[pos_j] = i

        super().swap(i, j)

    def __contains__(self, item):
        return item in self.mElementsMap

    def insert(self, *k):
        el = PQElement(k[0], k[1])
        if k[0] in self:
            self.decreasePriority(k[0], k[1])
        else:
            self.mSize += 1
            self.mItems.append(el)
            self.mElementsMap[k[0]] = self.mSize

            self.siftUp()

    def decreasePriority(self, item, priority):
        i = self.mElementsMap[item]
        if self.mItems[i][1] < 0:
            return True
        self.mItems[i].setPriority(self.mItems[i][1] + priority)

        if self.isRoot(i):
            while (2 * i) <= self.mSize:
                left = 2 * i
                right = 2 * i + 1
                min_child = self.maxChild(left, right)
                if self.mItems[i] < self.mItems[min_child]:
                    self.swap(min_child, i)
                i = min_child
        elif self.mItems[i] > self.mItems[self.getParent(i)]:
            while i > 1:
                parent = i // 2
                if self.mItems[i] > self.mItems[parent]:
                    self.swap(parent, i)
                i = parent
        else:
            while (2 * i) <= self.mSize:
                left = 2 * i
                right = 2 * i + 1
                min_child = self.maxChild(left, right)
                if self.mItems[i] < self.mItems[min_child]:
                    self.swap(min_child, i)
                i = min_child

        return True


    def extractMax(self):
        max_el = self.mItems[1]
        if max_el[1] > 0:
            return max_el[0]

    def __str__(self):
        res = ""
        for i in range(1, self.mSize + 1):
            res += str(self.mItems[i]) + "\n"
        return res

n = int(input())
que = PriorityQueue()

for i in range(n):
    try:
        st = input().split()
    except:
        break
    if st[0] == '+':
        que.insert(st[1], 1)
        print(que.extractMax())
    elif st[0] == '-':
        que.decreasePriority(st[1], -1)
        x = que.extractMax()
        print(0 if x is None else x)
