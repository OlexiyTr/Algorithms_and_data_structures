class Node:
    def __init__(self, item):
        self.mItem = item
        self.mNext = None

class Stack:
    mTopNode: Node
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
            raise Exception("Stack: 'pop' applied to empty container")
        current_top = self.mTopNode
        item = current_top.mItem
        self.mTopNode = self.mTopNode.mNext
        del current_top
        return item

    def top(self):
        if self.empty():
            raise Exception("Stack: 'top' applied to empty container")
        return self.mTopNode.mItem

check = Stack()

def try_to_check(a, b, s=''):
    if a + b == 0:
        print(s)
        return
    if a:
        check.push(0)
        try_to_check(a - 1, b, s + '(')
        check.pop()
        check.push(1)
        try_to_check(a - 1, b, s + '[')
        check.pop()
    if not(check.empty()):
        if check.top():
            check.pop()
            try_to_check(a, b - 1, s + ']')
            check.push(1)
        else:
            check.pop()
            try_to_check(a, b - 1, s + ')')
            check.push(0)


n = int(input())
z = n//2
try_to_check(z, z)
