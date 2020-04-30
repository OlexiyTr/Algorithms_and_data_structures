class Node:
    def __init__(self, item):
        self.mItem = item
        self.mNext = None
        self.mPrev = None


class Deque:
    def __init__(self):
        self.mFront = None
        self.mBack = None
        self._size  = 0

    def empty(self):
        return self.mFront is None

    def push_front(self, item):
        node = Node(item)
        node.mNext = self.mFront
        if not self.empty():
            self.mFront.mPrev = node
        else:
            self.mBack = node
        self.mFront = node
        self._size  += 1
        print('ok')

    def pop_front(self):
        if self.empty():
            return 'error'
        node = self.mFront
        item = node.mItem
        self.mFront = node.mNext
        if self.mFront is None:
            self.mBack = None
        else:
            self.mFront.mPrev = None
        del node
        self._size  -= 1
        return item

    def push_back(self, item):
        elem = Node(item)
        elem.mPrev = self.mBack
        if not self.empty():
            self.mBack.mNext = elem
        else:
            self.mFront = elem
        self.mBack = elem
        self._size  += 1
        print('ok')

    def pop_back(self):
        if self.empty():
            return 'error'
        node = self.mBack
        item = node.mItem
        self.mBack = node.mPrev
        if self.mBack is None:
            self.mFront = None
        else:
            self.mBack.mNext = None
        del node
        self._size  -= 1
        return item

    def __del__(self):
        while self.mFront is not None:
            node = self.mFront
            self.mFront = self.mFront.mNext
            del node
        self.mBack = None

    def clear(self):
        self.mFront = None
        self.mBack = None
        self._size  = 0
        print('ok')

    def front(self):
        if self.empty():
            return 'error'
        return self.mFront.mItem

    def back(self):
        if self.empty():
            return 'error'
        return self.mBack.mItem

    def size(self):
        return self._size

    def exit(self):
        print('bye')

deq = Deque()

while True:
    try:
        st = input().split()
    except:
        break
    if st[0] == 'push_front':
        deq.push_front(int(st[1]))
    elif st[0] == 'push_back':
        deq.push_back(int(st[1]))
    elif st[0] == 'pop_front':
        print(deq.pop_front())
    elif st[0] == 'pop_back':
        print(deq.pop_back())
    elif st[0] == 'front':
        print(deq.front())
    elif st[0] == 'back':
        print(deq.back())
    elif st[0] == 'size':
        print(deq.size())
    elif st[0] == 'clear':
        deq.clear()
    else:
        deq.exit()
        break
