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

def bracketsChecker(brackets_sequence):
    s = Stack()
    for bracket in brackets_sequence:
        if bracket == "(" or bracket == "[":
            s.push(bracket)
        else:
            if not(s.empty()) and ((bracket == ')' and s.top() == '(') or (bracket == ']' and s.top() == '[')):
                s.pop()
            else:
                return False

    return s.empty()

n = int(input())

for i in range(n):
    if bracketsChecker(input()):
        print('Yes')
    else:
        print('No')
