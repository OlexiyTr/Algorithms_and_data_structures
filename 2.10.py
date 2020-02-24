import numpy
from random import randint

def binarySearch(array, el):
	    if len(array) == 0:
	        return False
	    else:
	        m = len(array) // 2
	        if array[m] == el:
	          return True
	        else:
	          if el < array[m]:
	            return binarySearch(array[:m], el)
	          else:
	            return binarySearch(array[m+1:], el)


arr = numpy.random.randint(0, 100, 100)
arr.sort()
print(arr, end = '\n\n')
x = randint(0, 100)
print(f'x = {x}')
print(f'result = {binarySearch(arr, x)}')

def binarySearch_2(array, el, start, stop):
    if start == stop:
        if array[start-1] == el:
            return start
        else:
            return None
    else:
        m = start + (stop - start) // 2
        if el < array[m]:
            return binarySearch_2(array, el, start, m)
        else:
            return binarySearch_2(array, el, m + 1, stop)

arr = numpy.random.randint(0, 100, 100)
arr.sort()
print(arr, end = '\n\n')
x = randint(0, 100)
print(f'x = {x}')
print(f'result = {binarySearch_2(arr, x, 0, len(arr) - 1)}')
