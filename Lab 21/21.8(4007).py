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

class Queue:

    def __init__(self):
        self.mFront = None
        self.mBack = None

    def empty(self):
        return self.mFront is None and self.mBack is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.empty():
            self.mFront = new_node
        else:
            self.mBack.mNext = new_node

        self.mBack = new_node

    def dequeue(self):
        if self.empty():
            raise Exception("Queue: 'dequeue' applied to empty container")

        current_front = self.mFront
        item = current_front.mItem
        self.mFront = self.mFront.mNext
        del current_front

        if self.mFront is None:
            self.mBack = None
        return item

def Add(n): return n+1000 if n//1000!=9 else n
def Minus(n): return n-1 if n%10!=1 else n
def ShiftLeft(n): return (n%1000)*10 + n//1000
def ShiftRight(n): return (n%10)*1000 + n//10
op = [Add, Minus, ShiftLeft, ShiftRight]

def waySearch(start, end):
    sources = {start: None}

    q = Queue()
    q.enqueue(start)

    while not q.empty():
        current = q.dequeue()
        if current == end:
            break
        for i in range(4):
            next = op[i](current)
            if next not in sources:
                q.enqueue(next)
                sources[next] = current


    if end not in sources:
        return None

    stack = Stack()
    current = end
    while current != start:
        stack.push(current)
        current = sources[current]
    stack.push(current)

    while not stack.empty():
        print(stack.pop())

x = int(input())
y = int(input())
waySearch(x,y)
