from copy import deepcopy
import sys

sys.setrecursionlimit(1500)

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
        current_top = self.mTopNode
        item = current_top.mItem
        self.mTopNode = self.mTopNode.mNext
        del current_top
        return item

    def top(self):
        return self.mTopNode.mItem if not self.empty() else None


st = input()
counter = 0

def bracketsChecker(s, n, bracket, l):
    global counter
    if l >len(st)/2:
        return 0
    if bracket == "(":
        s.push(bracket)
    else:
        if not(s.empty()) and s.top() == '(':
            s.pop()
        else:
            return 0
    if n == len(st)-1:
        if s.empty():
            return 1
        return 0
    if st[n+1] == '(':
        return bracketsChecker(deepcopy(s), n+1, '(',l+1)
    elif st[n+1] == ')':
        return bracketsChecker(deepcopy(s), n+1, ')',l)
    else:
        return bracketsChecker(deepcopy(s), n+1, '(',l+1) + bracketsChecker(deepcopy(s), n+1, ')',l)

print(bracketsChecker(Stack(), 0, '(' if st[0] == '?' else st[0],0))
