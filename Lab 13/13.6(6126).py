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
        print('ok')

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

    def clear(self):
        self.mFront = None
        self.mBack = None
        self._size  = 0
        print('ok')
        '''
        while not(self.empty()):
            self.pop()
        '''

    def exit(self):
        print('bye')

que = Queue()

while True:
    try:
        st = input().split()
    except:
        break
    if st[0] == 'push':
        que.push(int(st[1]))
    elif st[0] == 'pop':
        print(que.pop())
    elif st[0] == 'front':
        print(que.front())
    elif st[0] == 'size':
        print(que.size())
    elif st[0] == 'clear':
        que.clear()
    else:
        que.exit()
        break
