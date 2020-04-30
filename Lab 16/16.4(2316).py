class BinaryTree:

    def __init__(self, key):
        self.mKey = key
        self.mLeftChild = None
        self.mRightChild = None
        self.mParent = None

    def hasLeft(self) -> bool: return self.mLeftChild is not None
    def hasRight(self) -> bool: return self.mRightChild is not None
    def hasNoChildren(self) -> bool: return self.mLeftChild is None and self.mRightChild is None
    def removeLeft(self): self.mLeftChild = None
    def removeRight(self): self.mRightChild = None
    def __str__(self): return str(self.mKey)
    def isLeftChild(self): return self.mParent and self.mParent.mLeftChild == self
    def isRightChild(self): return self.mParent and self.mParent.mRightChild == self

    def setNode(self, item):
        if isinstance(item, BinaryTree):
            self.mKey = item.mKey
            self.mLeftChild = item.mLeftChild
            self.mRightChild = item.mRightChild
            if self.mLeftChild != None:
                self.mLeftChild.mParent = self
            if self.mRightChild != None:
                self.mRightChild.mParent = self
        else:
            self.mKey = item

    def setLeft(self, item):
        if isinstance(item, BinaryTree):
            self.mLeftChild = item
        elif self.hasLeft():
            self.mLeftChild.setNode(item)
        else:
            self.mLeftChild = BinaryTree(item)
        self.mLeftChild.mParent = self

    def setRight(self, item):
        if isinstance(item, BinaryTree):
            self.mRightChild = item
        elif self.hasRight():
            self.mRightChild.setNode(item)
        else:
            self.mRightChild = BinaryTree(item)
        self.mRightChild.mParent = self

    def removeSelfFromParent(self):
        if self.mParent is not None:
            if self.isLeftChild():
                self.mParent.mLeftChild = None
            else:
                self.mParent.mRightChild = None


class SearchTree(BinaryTree):

    def insert(self, key):
        self._insert_helper(self, key)

    def search(self, key):
        return self._search_helper(self, key)

    def getHeight(self):
        return self._height(self)

    def getCount(self):
       return self._count(self)

    @staticmethod
    def _height(root):
        left_height = SearchTree._height(root.mLeftChild) if root.hasLeft() else 0
        right_height = SearchTree._height(root.mRightChild) if root.hasRight() else 0
        return max(left_height, right_height) + 1

    @staticmethod
    def _count(node):
        left_count = SearchTree._count(node.mLeftChild) if node.hasLeft() else 0
        right_count = SearchTree._count(node.mRightChild) if node.hasRight() else 0
        return left_count + right_count + 1

    @staticmethod
    def _insert_helper(root, key):
        if root.mKey > key:
            if root.hasLeft():
                SearchTree._insert_helper(root.mLeftChild, key)
            else:
                root.setLeft(key)
        elif root.mKey < key:
            if root.hasRight():
                SearchTree._insert_helper(root.mRightChild, key)
            else:
                root.setRight(key)

    @staticmethod
    def _search_helper(root, key):
        if root.mKey == key:
            return root
        elif key < root.mKey:
            return SearchTree._search_helper(root.mLeftChild, key) if root.hasLeft() else None
        else:
            return SearchTree._search_helper(root.mRightChild, key) if root.hasRight() else None


    @staticmethod
    def _search_max(root):
        return SearchTree._search_max(root.mRightChild) if root.hasRight() else root

    @staticmethod
    def _search_min(root):
        return SearchTree._search_min(root.mLeftChild) if root.hasLeft() else root

    def addItems(self, *items):
        for item in items:
            self.insert(item)

    def getSecondMax(self):
        node = self
        lst = [node.mKey]
        while node.hasRight():
            node = node.mRightChild
            lst.append(node.mKey)
        lst.pop()
        while True:
            if node.hasRight():
                node = node.mRightChild
                lst.append(node.mKey)
            elif node.hasLeft():
                node = node.mLeftChild
                lst.append(node.mKey)
            else:
                break
        return max(lst)

    def getLeaves(self):
        leaves = []
        def DFS(node):
            if node.hasLeft():
                DFS(node.mLeftChild)
            if node.hasRight():
                DFS(node.mRightChild)
            if not (node.hasLeft() or node.hasRight()):
                leaves.append(node.mKey)
        DFS(self)
        return leaves

nodes = tuple(map(int, input().split()))
if nodes[0] == 0:
    pass
else:
    root = SearchTree(nodes[0])
    i = 1
    while nodes[i] != 0:
        root.insert(nodes[i])
        i += 1
    print(*root.getLeaves())
