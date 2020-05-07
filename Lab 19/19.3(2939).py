from math import log2, ceil

class SegmentTree:

    def __init__(self, array):
        k = len(array)
        n = 1 << ceil(log2(k))
        self.mItems = n * [0] + array + (n - k) * [0]

        for i in range(n - 1, 0, -1):
            self.mItems[i] = self.mItems[2 * i] + self.mItems[2 * i + 1]

        self.mSize = n

    def update(self, left, right, item):
        left += self.mSize
        right += self.mSize
        for i in range(left, right + 1):
            self.mItems[i] = item
        while left > 0:
            left = left // 2
            right = right // 2
            self.mItems[left] = self.mItems[left * 2] + self.mItems[left * 2 + 1]
            self.mItems[right] = self.mItems[right * 2] + self.mItems[right * 2 + 1]
            item = self.mItems[left * 2 + 2] + self.mItems[left * 2 + 3]
            for i in range(left + 1, right):
                self.mItems[i] = item

    def sum(self, left, right):
        left += self.mSize
        right += self.mSize

        res = 0

        while left <= right:
            if left % 2 == 1:
                res += self.mItems[left]
            if right % 2 == 0:
                res += self.mItems[right]

            left = (left + 1) // 2
            right = (right - 1) // 2

        return res

    def __setitem__(self, key, value):
        self.update(key, value)

    def __getitem__(self, item):
        item += self.mSize
        return self.mItems[item]

    def __call__(self, left, right):
        return self.sum(left, right)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
tree = SegmentTree(arr)
for _ in range(m):
    st = input().split()
    if st[0] == '=':
        tree.update(int(st[1]) - 1, int(st[2]) - 1, int(st[3]))
    elif st[0] == '?':
        print(tree.sum(int(st[1]) - 1, int(st[2]) - 1))
