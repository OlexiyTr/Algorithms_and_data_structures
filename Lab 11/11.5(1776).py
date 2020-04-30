class Node:

    def __init__(self, item):
        self.mItem = item
        self.mNext = None


class Stack:
    def __init__(self):
        self.mTopNode = None

    def empty(self) -> bool:
        return self.mTopNode is None

    def push(self, item):
        new_node = Node(item)
        if not self.empty():
            new_node.mNext = self.mTopNode
        self.mTopNode = new_node

    def pop(self):
        if self.empty():
            return 'error'
        current_top = self.mTopNode
        item = current_top.mItem
        self.mTopNode = self.mTopNode.mNext
        del current_top
        return item

    def back(self):
        if self.empty():
            return 'error'
        item = self.mTopNode.mItem
        return item

    def clear(self):
        while not self.empty():
            self.pop()

    def top(self):
        return self.mTopNode.mItem

s = Stack()

while True:
    n = int(input())
    if n == 0:
        break
    while True:
        lst = list(map(int,input().split()))
        if lst[0]==0:
            break
        s.clear()
        cur = 1
        ans = True
        for i in range(1,n):
            while cur <= lst[i-1]:
                s.push(cur)
                cur += 1
            if s.top()!=lst[i-1]:
                ans = False
            s.pop()
        if ans:
            print('Yes')
        else:
            print('No')
    print('')
