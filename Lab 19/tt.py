from math import log2, ceil

class SegmentTree:
    ''' Дерево відрізків з операцією суми.'''

    def __init__(self, array):
        k = len(array)
        n = 1 << ceil(log2(k))
        self.items = n * [0] + array + (n - k) * [0]
        for i in range(n - 1, 0, -1):
            # Визначаємо навантаження предків
            self.items[i] = self.items[i * 2] + self.items[i * 2 + 1]
        self.size = n

    def update(self, i, item):
        ''' Міняє елемент масиву на позиції i (початок з нуля) на item.'''
        i += self.size
        self.items[i] = item
        while i != 1:  # Поки не дійшли до кореня
            i = i // 2 # Беремо номер батька
            # Визначаємо його навантаження
            self.items[i] = self.items[i * 2] + self.items[i * 2 + 1]

    def sum(self, left, right):
        print( left, right)
        ''' Повертає суму елементів відрізка.'''
        left += self.size
        right += self.size
        result = 0
        while left <= right:
            if left % 2 == 1: # Якщо правий син
                result += self.items[left]
            if right % 2 == 0: # Якщо лівий син
                result += self.items[right]
            left = (left + 1) // 2   # Беремо індекс батька вузла справа
            right = (right - 1) // 2 # Беремо індекс батька вузла зліва
        return result


n, m = map(int, input().split())
arr = list(map(int, input().split()))
tree = SegmentTree(arr)
for _ in range(m):
    st = input().split()
    if st[0] == '=':
        tree.update(int(st[1]) - 1, int(st[2]))
    elif st[0] == '?':
        print(tree.sum(int(st[1]) - 1, int(st[2])) - 1)
