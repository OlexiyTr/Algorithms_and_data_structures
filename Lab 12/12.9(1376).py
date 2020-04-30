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
    if dec_number == 'ERROR':
        return 'ERROR'
    stack = Stack()
    while dec_number > 0:
        stack.push(dec_number % base)
        dec_number //= base

    converted = ""
    while not stack.empty():
        converted = converted + getCharDigit(stack.pop())

    return converted

def bin_to_dec(digit, base):
    counter = 0
    l = len(digit)
    number = 0
    if base <= 10:
        for i in range(0, l):
            if '0'<=digit[i]<=str(base-1) and counter <= 10:
                counter += 1
                number += int(digit[i])*(base**(l-i-1))
            else: return 'ERROR'
    else:
        for i in range(0, l):
            if '0'<=digit[i]<='9' and counter <= 10:
                counter += 1
                number += int(digit[i])*(base**(l-i-1))
            elif 'A'<=digit[i]<=chr(base + ord('A') - 11):
                number += int(ord(digit[i]) - ord("A") + 10)*(base**(l-i-1))
            else: return 'ERROR'
    return number

while True:
    try:
        m,k,num = input().split()
    except:
        break
    res = convert(bin_to_dec(num,int(m)),int(k))

    if res == 'ERROR':
        print(f"{num} is an illegal base {m} number")
    else:
        print(f"{num} base {m} = {res} base {k}")
