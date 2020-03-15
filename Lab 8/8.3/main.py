import time

import numpy
import user

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

def checkResult(array):
    """ Перевіряє впорядкованість масиву даних за зростанням
    :param array: масив
    """
    errors = 0
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            errors += 1

    print("Errors:       ", errors)


def testSort(base, sort):
    s = numpy.copy(base)
    t = time.process_time()
    sort(s)
    dt = time.process_time() - t
    print('Sorting method: ', sort)
    print('Sorting time: ', dt)
    checkResult(s)


sorting_method = [user.bubble_sort,
                  user.bubble_sort_optimized,
                  user.selection_sort,
                  user.insertion_sort,
                  user.merge_sort,
                  user.quick_sort]


def test():
    base = numpy.random.randint(0, 100000, user.N)

    print(" == Randomly generated array == ")
    for func in sorting_method:
        testSort(base, func)

    sorted_increasing = numpy.copy(base)
    sorted_increasing.sort()
    print("\n == Sorted (inc) array == ")
    for func in sorting_method:
        testSort(sorted_increasing, func)

    sorted_decreasing = sorted_increasing[::-1]
    print("\n == Sorted (dec) array == ")
    for func in sorting_method:
        testSort(sorted_decreasing, func)


if __name__ == "__main__":
    test()
