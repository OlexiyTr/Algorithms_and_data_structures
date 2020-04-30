class Node:
    def __init__(self, key, parent):
        self.mParent = parent
        self.mKey = key

    def setKey(self, key): self.mKey = key
    def key(self): return self.mKey
    def parent(self): return self.mParent
    def setParent(self, parent): self.mParent = parent
    def __str__(self): return str(self.mKey)

class Tree(Node):

    def __init__(self, key, parent=None):
        super().__init__(key, parent)
        self.mChildren = []

    def addChild(self, child):
        child.mParent = self
        self.mChildren.append(child)

    def getChild(self, key):
        for child in self.mChildren:
            if child.key() == key:
                return child
        return None

    def getChildren(self):
        return self.mChildren

    def clear(self):
        self.mChildren.clear()

    def haschild(self, digit):
        for child in self.mChildren:
            if child.key() == digit:
                return True
        return False

    def haschildren(self):
        return bool(self.mChildren)

    def BFS(self, key):
        queue = []
        queue.append(self)
        while queue:
            node = queue.pop(0)
            if node.key() == key:
                return node
            for child in node.mChildren:
                queue.append(child)
        return

    def add(self, parent_key, child_key):
        parent = self.BFS(parent_key)
        parent.addChild(Tree(child_key))

    def get(self, i, j):
        node_i = self.BFS(i)
        node_j = self.BFS(j)
        while True:
            while node_j.key() >= node_i.key():
                if node_i is node_j:
                    return node_i.key()
                node_j = node_j.parent()
            node_i = node_i.parent()

    def __str__(self):
        return super().__str__() + " : " + str([el.key() for el in self.mChildren])

tree = Tree(1)

k = int(input())
for _ in range(k):
    st = input().split()
    if st[0] == 'ADD':
        tree.add(int(st[1]), int(st[2]))
    elif st[0] == 'GET':
        print(tree.get(int(st[1]), int(st[2])))
