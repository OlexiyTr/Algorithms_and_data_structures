import sys

sys.setrecursionlimit(1500)

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

def search_2(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i

def buildTree(inOrder, preOrder, inStrt, inEnd):
    if (inStrt > inEnd):
            return None
    mTree = SearchTree(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    if inStrt == inEnd:
        return mTree
    inIndex = search_2(inOrder, inStrt, inEnd, mTree.mKey)

    mTree.mLeftChild = buildTree(inOrder, preOrder, inStrt, inIndex-1)
    mTree.mRightChild = buildTree(inOrder, preOrder, inIndex + 1, inEnd)

    return mTree

string = ''

def DFS(root):
    global string
    if root.hasLeft():
        DFS(root.mLeftChild)

    if root.hasRight():
        DFS(root.mRightChild)

    string += root.mKey


num = int(input())

for _ in range(num):
    string = ''
    st = input().split()
    buildTree.preIndex = 0
    root = buildTree(list(st[2]), list(st[1]) , 0, len(st[2])-1)
    DFS(root)
    print(string)
