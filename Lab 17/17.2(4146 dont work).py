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
    def isLeftChild(self): return self is self.mParent.mLeftChild
    def isRightChild(self): return self is self.mParent.mRightChild

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

    def addItems(self, items):
        for item in items:
            self.insert(item)

    def isBalanced(self):
        return 1 if SearchTree._balanced(self) else 0

    @staticmethod
    def _balanced(root):
        left_height = SearchTree._balanced(root.mLeftChild) if root.hasLeft() else 0
        if left_height is False:
            return False
        right_height = SearchTree._balanced(root.mRightChild) if root.hasRight() else 0
        if right_height is False:
            return False
        if abs(left_height - right_height) > 1:
            return False
        return max(left_height, right_height) + 1

class AVLTree(SearchTree):

    def __init__(self, key):
        super().__init__(key)
        self.mBalanceFactor = 0
        self.mIsRoot = False

    def isRoot(self):
        return isinstance(self.mParent, Tree)

    def setLeft(self, item):
        if isinstance(item, AVLTreeWithDelete):
            self.mLeftChild = item
        elif self.hasLeft():
            self.mLeftChild.setNode(item)
        else:
            self.mLeftChild = AVLTreeWithDelete(item)
        self.mLeftChild.mParent = self
        AVLTree.updateBalance(self.mLeftChild)

    def setRight(self, item):
        if isinstance(item, AVLTreeWithDelete):
            self.mRightChild = item
        elif self.hasRight():
            self.mRightChild.setNode(item)
        else:
            self.mRightChild = AVLTreeWithDelete(item)
        self.mRightChild.mParent = self
        AVLTree.updateBalance(self.mRightChild)


    @staticmethod
    def updateBalance(node):
        if node.mBalanceFactor > 1 or node.mBalanceFactor < -1:
            AVLTree.rebalance(node)
            return
        if not node.isRoot():
            if node.isLeftChild():
                node.mParent.mBalanceFactor += 1
            elif node.isRightChild():
                node.mParent.mBalanceFactor -= 1

            if node.mParent.mBalanceFactor != 0:
                AVLTree.updateBalance(node.mParent)

    @staticmethod
    def rebalance(node):
        if node.mBalanceFactor < 0:
            if node.mRightChild.mBalanceFactor > 0:
                AVLTree.rotateRight(node.mRightChild)
                AVLTree.rotateLeft(node)
            else:
                AVLTree.rotateLeft(node)
        elif node.mBalanceFactor > 0:
            if node.mLeftChild.mBalanceFactor < 0:
                AVLTree.rotateLeft(node.mLeftChild)
                AVLTree.rotateRight(node)
            else:
                AVLTree.rotateRight(node)

    @staticmethod
    def rotateLeft(node):
        node_parent = node.mParent
        if node.isRoot():
            node_parent.root = AVLTree.__rotateLeft(node)
        elif node.isLeftChild():
            node_parent.mLeftChild = AVLTree.__rotateLeft(node)
        elif node.isRightChild():
            node_parent.mRightChild = AVLTree.__rotateLeft(node)

    @staticmethod
    def __rotateLeft(root):
        pivot = root.mRightChild
        root.mRightChild = pivot.mLeftChild

        if pivot.hasLeft():
            pivot.mLeftChild.mParent = root

        pivot.mLeftChild = root

        node_parent = root.mParent
        root.mParent = pivot
        pivot.mParent = node_parent

        root.mBalanceFactor = root.mBalanceFactor + 1 - min(0, pivot.mBalanceFactor)
        pivot.mBalanceFactor = pivot.mBalanceFactor + 1 + max(0, root.mBalanceFactor)

        return pivot

    @staticmethod
    def rotateRight(node):
        node_parent = node.mParent
        if node.isRoot():
            node_parent.root = AVLTree.__rotate_right(node)
        elif node.isLeftChild():
            node_parent.mLeftChild = AVLTree.__rotateRight(node)
        elif node.isRightChild():
            node_parent.mRightChild = AVLTree.__rotateRight(node)

    @staticmethod
    def __rotateRight(root):
        pivot = root.mLeftChild
        root.mLeftChild = pivot.mRightChild

        if pivot.mRightChild:
            pivot.mRightChild.mParent = root

        pivot.mRightChild = root

        node_parent = root.mParent
        root.mParent = pivot
        pivot.mParent = node_parent

        root.mBalanceFactor = root.mBalanceFactor - 1 - max(pivot.mBalanceFactor, 0)
        pivot.mBalanceFactor = pivot.mBalanceFactor - 1 + min(root.mBalanceFactor, 0)

        return pivot

class AVLTreeWithDelete(AVLTree):

    def __init__(self, key):
        super().__init__(key)

    def delete(self, key):
        self._delete_helper(self, key)

    @staticmethod
    def _delete_helper(root, key):
        node = root.search(key)

        if node is None or node.mIsRoot:
            return

        parent = node.mParent
        if node.hasNoChildren():
            if node.isRoot():
                parent.root = None
            elif node.isLeftChild():
                parent.mLeftChild = None
                AVLTreeWithDelete.updateBalanceOnDelete(parent, True)
            elif node.isRightChild():
                parent.mRightChild = None
                AVLTreeWithDelete.updateBalanceOnDelete(parent, False)

        elif node.hasLeft() and not node.hasRight():
            if node.isRoot():
                parent.root = node.mLeftChild
                node.mLeftChild.mParent = parent
            else:
                node.setNode(node.mLeftChild)
                AVLTreeWithDelete.updateBalanceOnDelete(parent, True)

        elif node.hasRight() and not node.hasLeft():
            if node.isRoot():
                parent.root = node.mRightChild
                node.mRightChild.mParent = parent
            else:
                node.setNode(node.mRightChild)
                AVLTreeWithDelete.updateBalanceOnDelete(parent, False)

        else:
            left_max = AVLTreeWithDelete._search_max(node.mLeftChild)
            left_max_key = left_max.mKey
            AVLTreeWithDelete._delete_helper(node.mLeftChild, left_max_key)
            node.setNode(left_max_key)

    @staticmethod
    def updateBalanceOnDelete(node, came_from_left):

        if node is None or node.mIsRoot:
            return

        if came_from_left:
            node.mBalanceFactor -= 1
        else:
            node.mBalanceFactor += 1

        if node.mBalanceFactor > 1 or node.mBalanceFactor < -1:
            AVLTree.rebalance(node)
            if node.mParent is not None:
                if node.parent.balance == 0 and node.mParent.mParent is not None:
                    node.parent.parent.update_balance_on_delete(node.parent.is_left())

        elif not node.isRoot() and node.mBalanceFactor == 0:
            AVLTreeWithDelete.updateBalanceOnDelete(node.mParent, node.isLeftChild())


class Tree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, key):
        if self.is_empty():
            self.root = AVLTreeWithDelete(key)
            self.root.mParent = self
        else:
            self.root.insert(key)

    def exists(self, key):
        if self.is_empty():
            return 'false'
        else:
            return 'true' if self.root.search(key) is not None else 'false'

    def delete(self, key):
        if not self.is_empty():
            self.root.delete(key)



root = Tree()

while True:
    try:
        st, x = input().split()
    except:
        break
    if st == 'insert':
        root.insert(int(x))
    elif st == 'delete':
        root.delete(int(x))
    elif st == 'exists':
        print(root.exists(int(x)))
