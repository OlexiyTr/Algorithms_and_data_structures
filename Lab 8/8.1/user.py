
"""
Реалізуйте підпрограму сортування масиву.
"""

'''
result::    Sorting time:  24.359375
            Errors:        0
'''

N = 1000000

def sort(array):
    """ Сортування масиву
    :param array: Вхідний масив даних, що треба відсортувати.
    """
    if len(array) > 1:
        mid = len(array) // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]
        sort(lefthalf)
        sort(righthalf)
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
