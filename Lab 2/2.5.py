n = int(input())
n_lst = list(map(int, input().split()))

m = int(input())
m_lst = list(map(int, input().split()))

def binary_search(array, x):
    left = 0
    right = len(array) - 1

    while left < right:
        mid = left + (right - left) // 2
        if x > array[mid]:
            left = mid + 1
        else:
            right = mid

    return array[right] == x

for el in m_lst:
    if binary_search(n_lst, el):
        print("YES")
    else:
        print("NO")
