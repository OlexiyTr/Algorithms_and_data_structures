n = int(input())
array = []
for i in range(n):
    array.append(input())

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
            break

sort1(array)

for i in range(n):
    print(array[i])
