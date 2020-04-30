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

def getCharDigit(digit):
    assert digit <= 16
    if digit <= 9:
        str_digit = str(digit)
    else:
        str_digit = chr(ord("A") + digit - 10)
    return str_digit

def convert(dec_number, base):
    assert 2 <= base <= 16
    stack = Stack()
    while dec_number > 0:
        stack.push(dec_number % base)
        dec_number //= base

    converted = ""
    while not stack.empty():
        converted = converted + getCharDigit(stack.pop())

    return converted

def bin_to_dec(digit):
    l = len(digit)
    number = 0
    for i in range(0, l):
        number += int(digit[i])*(2**(l-i-1))
    return number


while True:
    try:
        num = bin_to_dec(input())
        print(convert(num,16))
    except:
        break
