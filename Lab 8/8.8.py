n, m = map(int,input().split())
arr = list(map(int,input().split()))

def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        if array[i] > array[i + 1]:
            if array[i]+array[i + 1]>m:
                return False
            array[i], array[i + 1] = array[i + 1], array[i]
    return True

if bubble_sort(arr):
    print('Yes')
else:
    print('No')
