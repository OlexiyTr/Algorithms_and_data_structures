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
        if self.empty():
            return 'error'
        current_front = self.mFront
        item = current_front.mItem
        self.mFront = self.mFront.mNext
        del current_front
        if self.mFront is None:
            self.mBack = None
        self._size -= 1
        return item

    def front(self):
        if self.empty():
            return 'error'
        return self.mFront.mItem

    def size(self):
        return self._size

first = Queue()
second = Queue()
i = 0

n = int(input())
for el in map(int, input().split()):
    first.push(el)
for el in map(int, input().split()):
    second.push(el)

while i < 2*10**5:
    i += 1
    first_c = first.pop()
    second_c = second.pop()
    if first_c == 0 and second_c == n-1:
        first.push(first_c)
        first.push(second_c)
    elif first_c == n-1 and second_c == 0:
        second.push(first_c)
        second.push(second_c)
    elif first_c > second_c:
        first.push(first_c)
        first.push(second_c)
    else:
        second.push(first_c)
        second.push(second_c)
    if first.empty():
        print(f'second {i}')
        break
    elif second.empty():
        print(f'first {i}')
        break
