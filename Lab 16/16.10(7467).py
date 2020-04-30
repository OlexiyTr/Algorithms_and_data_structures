class BinaryTree:

    def __init__(self, key, value):
        self.mKey = key
        self.mLeftChild = None
        self.mRightChild = None
        self.mParent = None
        self.mValue = value

    def hasLeft(self) -> bool: return self.mLeftChild is not None
    def hasRight(self) -> bool: return self.mRightChild is not None
    def hasNoChildren(self) -> bool: return self.mLeftChild is None and self.mRightChild is None
    def removeLeft(self): self.mLeftChild = None
    def removeRight(self): self.mRightChild = None
    def __str__(self): return str(self.mKey)
    def isLeftChild(self): return self.mParent and self.mParent.mLeftChild == self
    def isRightChild(self): return self.mParent and self.mParent.mRightChild == self

    def setNode(self, item, value):
        if isinstance(item, BinaryTree):
            self.mKey = item.mKey
            self.mValue = item.mValue
            self.mLeftChild = item.mLeftChild
            self.mRightChild = item.mRightChild
            if self.mLeftChild != None:
                self.mLeftChild.mParent = self
            if self.mRightChild != None:
                self.mRightChild.mParent = self
        else:
            self.mKey = item
            self.mValue = value

    def setLeft(self, item, value):
        if isinstance(item, BinaryTree):
            self.mLeftChild = item
        elif self.hasLeft():
            self.mLeftChild.setNode(item, value)
        else:
            self.mLeftChild = BinaryTree(item, value)
        self.mLeftChild.mParent = self

    def setRight(self, item, value):
        if isinstance(item, BinaryTree):
            self.mRightChild = item
        elif self.hasRight():
            self.mRightChild.setNode(item, value)
        else:
            self.mRightChild = BinaryTree(item, value)
        self.mRightChild.mParent = self

    def removeSelfFromParent(self):
        if self.mParent is not None:
            if self.isLeftChild():
                self.mParent.mLeftChild = None
            else:
                self.mParent.mRightChild = None


class SearchTree(BinaryTree):

    def insert(self, key, value):
        self._insert_helper(self, key, value)

    def search(self, key):
        return self._search_helper(self, key)

    @staticmethod
    def _insert_helper(root, key, value):
        if root.mKey > key:
            if root.hasLeft():
                SearchTree._insert_helper(root.mLeftChild, key, value)
            else:
                root.setLeft(key, value)
        elif root.mKey < key:
            if root.hasRight():
                SearchTree._insert_helper(root.mRightChild, key, value)
            else:
                root.setRight(key, value)

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

    def addItems(self, items):
        for item in items:
            self.insert(item)

def is_mirror(root1 , root2):
    if root1 is None and root2 is None:
        return 1
    if (root1 is not None and root2 is not None):
            if  root1.mValue == root2.mValue:
                return (is_mirror(root1.mLeftChild, root2.mRightChild) and is_mirror(root1.mRightChild, root2.mLeftChild))
    return 0

def is_symmetric(root):
    return is_mirror(root, root)


num = int(input())
nodes = list(map(int, input().split()))
values = list(map(int, input().split()))

root = SearchTree(nodes[0], values[0])
for i in range(1, len(nodes)):
    root.insert(nodes[i], values[i])
print(is_symmetric(root))
