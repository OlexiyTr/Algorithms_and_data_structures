class Deque:
    def __init__(self):
        self.mItems = []

    def empty(self):
        return len(self.mItems) == 0

    def push_front(self, item):
        self.mItems.append(item)
        print('ok')

    def pop_front(self):
        return self.mItems.pop()

    def push_back(self, item):
        self.mItems.insert(0, item)
        print('ok')

    def pop_back(self):
        return self.mItems.pop(0)

    def __len__(self):
        return len(self.mItems)

    def front(self):
        return self.mItems[-1]

    def back(self):
        return self.mItems[0]

    def clear(self):
        self.mItems = []
        print('ok')

    def exit(self):
        print('bye')

deq = Deque()

while True:
    st = input().split()
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
        print(len(deq))
    elif st[0] == 'clear':
        deq.clear()
    else:
        deq.exit()
        break
