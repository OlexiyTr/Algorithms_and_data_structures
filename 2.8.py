import numpy
import matplotlib.pyplot as plt
from time import perf_counter

TIME = []


def find(array):
    i = 0
    l = len(array)
    res = []
    while i < l:
        if array[i] == (array[i] & ~(array[i] & (array[i] - 1))):
            res.append(array[i])
        i += 1
    return res

for i in range(4,10000):
    arr = numpy.random.randint(0, 1000, i)
    arr.sort()
    dt = perf_counter()
    find(arr)
    TIME.append(perf_counter() - dt)

plt.plot(TIME)   #Лінійне зростання
plt.show()
