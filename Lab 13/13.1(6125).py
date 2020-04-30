class Queue:
    def __init__(self):
        self.mItems = []

    def empty(self):
        return len(self.mItems) == 0

    def push(self, item):
        self.mItems.append(item)
        print('ok')

    def pop(self):
        return self.mItems.pop(0)

    def front(self):
        return self.mItems[0]

    def __len__(self):
        return len(self.mItems)

    def clear(self):
        self.mItems = []
        print('ok')

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
        print(len(que))
    elif st[0] == 'clear':
        que.clear()
    else:
        que.exit()
        break
