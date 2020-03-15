
"""
Реалізуйте підпрограму сортування масиву.
"""

'''
result::    Sorting time:  12.203125
            Errors:        0
'''

N = 1000000

def sort(array, a, b):
    """ Сортування масиву
    :param array: Вхідний масив даних, що треба відсортувати.
    """
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
    sort(array, a, right)
    sort(array, right + 1, b)
