import time

import numpy
import user

'''
result::    Sorting time:  12.203125
            Errors:        0
'''

def checkResult(array):
    """ Перевіряє впорядкованість масиву даних за зростанням
    :param array: масив
    """
    errors = 0
    for i in range(1, len(array)):
        if array[i-1] > array[i]:
            errors += 1

    print("Errors:       ", errors)


def testSort():

    s = numpy.random.randint(0, 100000, user.N)
    t = time.process_time()
    user.sort(s,0,len(s)-1)
    dt = time.process_time() - t
    print('Sorting time: ', dt)
    checkResult(s)


if __name__ == "__main__":
    testSort()
