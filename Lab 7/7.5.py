n = int(input())
array = list(map(int, input().split()))

def sort1(array):
    n = len(array)
    k = 0
    for pass_num in range(n - 1, 0, -1):
        counter = False
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                counter = True
                k += 1
                array[i], array[i + 1] = array[i + 1], array[i]
        if not(counter):
            return k
    return k

print(sort1(array))
