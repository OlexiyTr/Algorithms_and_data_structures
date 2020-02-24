"""
Знайдіть кількість входжень заданого числа x до впорядкованого за неспаданням масиву цілих чисел array
"""


def counter(array, x):
    """ кількість входжень заданого числа.
    :param array: Масив цілих чисел впорядкований за неспаданням
    :param x:     Шуканий елемент
    :return:      Кількість входжень
    """
    return  bsearch_rightmost(array, x) - bsearch_leftmost(array, x)

def bsearch_rightmost(array, x):
    left = 0
    right = len(array)
    while left < right:
        m = left + (right - left) // 2
        if array[m] <= x:
            left = m + 1
        else:
            right = m

    return left

def bsearch_leftmost(array, x):
    left = 0
    right = len(array)
    while left < right:
        m = left + (right - left) // 2
        if array[m] < x:
            left = m + 1
        else:
            right = m

    return left
