n = int(input())
arr = list(map(int, input().split()))

def quick_sort(array,a=None,b=None):
    """ Швидке сортування

        :param array: Масив (список однотипових елементів)
        :return: None
        """
    if a == None:
        a = 0
        b = len(array)-1
    if a >= b:
        return
    pivot = array[a + (b - a) // 2]
    left = a
    right = b
    while True:
        while array[left] < pivot:
            left += 1
        while pivot < array[right]:
            right -= 1

        if left >= right:
            break

        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    quick_sort(array, a, right)
    quick_sort(array, right + 1, b)

quick_sort(arr)

for i in range(n):
    print(arr[i], end= ' ')
