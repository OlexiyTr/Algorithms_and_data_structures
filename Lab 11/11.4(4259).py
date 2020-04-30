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
            new_node.mItem = min(new_node.mItem,self.mTopNode.mItem)
        self.mTopNode = new_node

    def pop(self):
        current_top = self.mTopNode
        item = current_top.mItem
        self.mTopNode = self.mTopNode.mNext
        del current_top
        return item

    def getMin(self):
        return self.mTopNode.mItem

s = Stack()

n = int(input())

for i in range(n):
    st = input().split()
    if st[0] == '1':
        s.push(int(st[1]))
    elif st[0] == '2':
        s.pop()
    else:
        print(s.getMin())
