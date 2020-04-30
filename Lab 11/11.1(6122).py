class Node:

    def __init__(self, item):
        self.mItem = item
        self.mNext = None


class Stack:
    def __init__(self):
        self.mTopNode = None
        self._size = 0

    def empty(self) -> bool:
        return self.mTopNode is None

    def push(self, item):
        new_node = Node(item)
        if not self.empty():
            new_node.mNext = self.mTopNode
        self.mTopNode = new_node
        self._size+=1
        print('ok')

    def pop(self):
        current_top = self.mTopNode
        item = current_top.mItem
        self.mTopNode = self.mTopNode.mNext
        self._size-=1
        del current_top
        return item

    def back(self):
        item = self.mTopNode.mItem
        return item

    def size(self):
        return self._size

    def clear(self):
        self._size = 0
        print('ok')

    def exit(self):
        print('bye')

s = Stack()

while True:
    try:
        st = input().split()
    except:
        break
    if st[0] == 'push':
        s.push(int(st[1]))
    elif st[0] == 'pop':
        print(s.pop())
    elif st[0] == 'back':
        print(s.back())
    elif st[0] == 'size':
        print(s.size())
    elif st[0] == 'clear':
        s.clear()
    else:
        s.exit()
        break
