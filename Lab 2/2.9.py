import numpy
import matplotlib.pyplot as plt
from time import perf_counter
from random import randint

TIME = []

def find(array, el):
    i = 0
    l = len(array)
    step = 10
    while i < l:
        if el <= array[i]:
            for j in range(i, i-step, -1):
                if array[j] == el:
                    return j
        i += step
    i -= step
    while i < l:
        if array[i] == el:
            return i
        i += 1
    return None

#test
#arr = numpy.random.randint(0, 100, 100)
#arr.sort()
#print(arr)
#print(find(arr, 16))
#print(arr[find(arr, 16)])

for i in range(4,10000):
    arr = numpy.random.randint(0, 1000, i)
    arr.sort()
    x = randint(0, 1000)
    dt = perf_counter()
    find(arr,x)
    TIME.append(perf_counter() - dt)

plt.plot(TIME)   #Значно швидше за 2.8, результат можно покращити єкспериментуючи
plt.show()       #із step. Але це все одно лінійна складність.
