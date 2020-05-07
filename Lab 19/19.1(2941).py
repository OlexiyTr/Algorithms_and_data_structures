from math import log2


class SegmentTree:

    def __init__(self, array):
        k = len(array)
        n = (1 << int(log2(k - 1)) + 1)
        self.mItems = 2 * n * [0]

        for i in range(k):
            self.mItems[n + i] = array[i]

        for i in range(n - 1, 0, -1):
            self.mItems[i] = self.mItems[2 * i] + self.mItems[2 * i + 1]

        self.mSize = n

    def update(self, pos, x):
        pos += self.mSize
        self.mItems[pos] = x

        i = pos // 2
        while i > 0:
            self.mItems[i] = self.mItems[2 * i] + self.mItems[2 * i + 1]
            i //= 2

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
        tree.update(int(st[1]) - 1, int(st[2]))
    elif st[0] == '?':
        print(tree(int(st[1]) - 1, int(st[2]) - 1))
