class Node:

    def __init__(self, key):
        self.mKey = key

    def setKey(self, key):
        self.mKey = key

    def key(self):
        return self.mKey

    def __str__(self):
        return str(self.mKey)

class Tree(Node):

    def __init__(self, key):
        super().__init__(key)
        self.mChildren = []

    def addChild(self, child):
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

    def addphone(self, phone: str):
        node = self
        i = 0
        while i < len(phone) and node.haschild(phone[i]): # Пробігаємо по ланцюжку існуючих дітей
            node = node.getChild(phone[i])
            i += 1
        if i == len(phone): # Якщо всі цифри номера вже є в довіднику, то даний номер є несумісним
            return False
        if i != 0 and not node.haschildren(): # Якщо в існуючому ланцюжку не залишилось дітей, то даний номер несумісний
                return False
        while i < len(phone): # Створюємо ланцюжок
            node.addChild(Tree(phone[i]))
            node = node.getChild(phone[i])
            i += 1
        return True

    def __str__(self):
        return super().__str__() + " : " + str([el.key() for el in self.mChildren])

tree = Tree('')

k = int(input())
for _ in range(k):
    n = int(input())
    flag = True
    for __ in range(n):
        number = input()
        if flag:
            flag = tree.addphone(number)
    print('YES') if flag else print('NO')
    tree.clear()
