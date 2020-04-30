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
        return self.mTopNode.mItem

def getCharDigit(digit):
    if digit <= 9:
        str_digit = str(digit)
    else:
        str_digit = chr(ord("A") + digit - 10)
    return str_digit

def convert(dec_number, base):
    stack = Stack()
    while dec_number > 0:
        stack.push(dec_number % base)
        dec_number //= base

    converted = ""
    while not stack.empty():
        converted = converted + getCharDigit(stack.pop())

    return converted

def bin_to_dec(digit, base):
    l = len(digit)
    number = 0
    for i in range(0, l):
        if '0'<=digit[i]<='9':
            number += int(digit[i])*(base**(l-i-1))
        else:
            number += int(ord(digit[i]) - ord("A") + 10)*(base**(l-i-1))
    return number

m, k = map(int, input().split())
num = input()
res = convert(bin_to_dec(num,m),k)
if res == '':
    print('0')
else:
    print(convert(bin_to_dec(num,m),k))
