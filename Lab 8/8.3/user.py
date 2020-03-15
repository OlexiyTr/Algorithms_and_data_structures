
"""
Реалізуйте підпрограми сортування масиву.
"""

'''
result::    == Randomly generated array ==
            Sorting method:  <function bubble_sort at 0x000001A138E8BF28>
            Sorting time:  39.625
            Errors:        0
            Sorting method:  <function bubble_sort_optimized at 0x000001A13FA2ABF8>
            Sorting time:  33.15625
            Errors:        0
            Sorting method:  <function selection_sort at 0x000001A13FABFA60>
            Sorting time:  16.765625
            Errors:        0
            Sorting method:  <function insertion_sort at 0x000001A13FABFAE8>
            Sorting time:  15.734375
            Errors:        0
            Sorting method:  <function merge_sort at 0x000001A13FABFB70>
            Sorting time:  0.125
            Errors:        0
            Sorting method:  <function quick_sort at 0x000001A13FABFBF8>
            Sorting time:  0.0625
            Errors:        0

            == Sorted (inc) array ==
            Sorting method:  <function bubble_sort at 0x000001A138E8BF28>
            Sorting time:  18.421875
            Errors:        0
            Sorting method:  <function bubble_sort_optimized at 0x000001A13FA2ABF8>
            Sorting time:  0.0
            Errors:        0
            Sorting method:  <function selection_sort at 0x000001A13FABFA60>
            Sorting time:  17.25
            Errors:        0
            Sorting method:  <function insertion_sort at 0x000001A13FABFAE8>
            Sorting time:  0.015625
            Errors:        0
            Sorting method:  <function merge_sort at 0x000001A13FABFB70>
            Sorting time:  0.1875
            Errors:        0
            Sorting method:  <function quick_sort at 0x000001A13FABFBF8>
            Sorting time:  0.0625
            Errors:        0

            == Sorted (dec) array ==
            Sorting method:  <function bubble_sort at 0x000001A138E8BF28>
            Sorting time:  48.625
            Errors:        0
            Sorting method:  <function bubble_sort_optimized at 0x000001A13FA2ABF8>
            Sorting time:  48.921875
            Errors:        0
            Sorting method:  <function selection_sort at 0x000001A13FABFA60>
            Sorting time:  16.78125
            Errors:        0
            Sorting method:  <function insertion_sort at 0x000001A13FABFAE8>
            Sorting time:  38.890625
            Errors:        0
            Sorting method:  <function merge_sort at 0x000001A13FABFB70>
            Sorting time:  0.125
            Errors:        0
            Sorting method:  <function quick_sort at 0x000001A13FABFBF8>
            Sorting time:  0.046875
            Errors:        0
'''

N = 10000     # Кількість елементів масиву.
              # Використовується у головній програмі для генерування
              # масиву з випадкових чисел


def bubble_sort(array):
    """ Сортування "Бульбашкою"

    :param array: Масив (список однотипових елементів)
    """
    n = len(array)
    for pass_num in range(n - 1, 0, -1):
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

def bubble_sort_optimized(array):
    """ Модификований алгоритм сортування "Бульбашкою"

    :param array: Вхідний масив даних, що треба відсортувати.
    """
    n = len(array)
    for pass_num in range(n - 1, 0, -1):
        c = True
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                c = False
                array[i], array[i + 1] = array[i + 1], array[i]
        if c:
            break


def selection_sort(array):
    """ Сортування вибором

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for i in range(n - 1, 0, -1):
        maxpos = 0
        for j in range(1, i + 1):
            if array[maxpos] < array[j]:
                maxpos = j
        array[i], array[maxpos] = array[maxpos], array[i]


def insertion_sort(array):
    """ Сортування вставкою

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for index in range(1, n):

        currentValue = array[index]
        position = index
        while position > 0:
            if array[position - 1] > currentValue:
                array[position] = array[position - 1]
            else:
                break
            position -= 1
        array[position] = currentValue


def merge_sort(array):
    """ Сортування злиттям

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    if len(array) > 1:
        mid = len(array) // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i += 1
            else:
                array[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            array[k] = righthalf[j]
            j += 1
            k += 1


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
