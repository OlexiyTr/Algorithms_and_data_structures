class Node:
    def __init__(self, item):
        self.mItem = item
        self.mNext = None

class Queue:
    def __init__(self):
        self.mFront = None
        self.mBack = None
        self._size  = 0

    def empty(self):
        return self.mFront is None

    def push(self, item):
        new_node = Node(item)
        if self.empty():
            self.mFront = new_node
        else:
            self.mBack.mNext = new_node
        self.mBack = new_node
        self._size += 1

    def pop(self):
        current_front = self.mFront
        item = current_front.mItem
        self.mFront = self.mFront.mNext
        del current_front
        if self.mFront is None:
            self.mBack = None
        self._size -= 1
        return item

    def front(self):
        return self.mFront.mItem

    def size(self):
        return self._size


qe = Queue()
n, k = map(int, input().split())

for i in range(n):
    qe.push(i+1)

i = n
counter = 0
while i != 1:
    person = qe.pop()
    counter += 1
    if counter == k:
        i -= 1
        counter = 0
    else:
        qe.push(person)

print(qe.pop())
