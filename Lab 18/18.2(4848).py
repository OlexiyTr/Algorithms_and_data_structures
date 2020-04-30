def heapSort(array):
    size = len(array)
    for i in range(size // 2 - 1, -1, -1):
        siftDown(array, i, size)
    for i in range(size - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        siftDown(array, 0, i)


def siftDown(array, start, end):
    while True:
        left = start * 2 + 1
        right = left + 1

        largest = start
        if left < end and array[left] > array[largest]:
            largest = left
        if right < end and array[right] > array[largest]:
            largest = right
        if largest == start:
            break

        array[start], array[largest] = array[largest], array[start]
        start = largest

st = list(map(int, input().split()))
heapSort(st)
print(*st)
