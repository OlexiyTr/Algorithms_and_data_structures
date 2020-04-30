def c_time(t):
    return int(t[0]) * 3600 + int(t[1]) * 60 + int(t[2])

n = int(input())
array =[]
for i in range(n):
    st = list(map(int,input().split()))
    array.append((st, c_time(st)))

def sort1(array):
    n = len(array)
    for index in range(1, n):

        currentValue = array[index]
        position = index
        c = False
        while position > 0:
            if array[position - 1][1] > currentValue[1]:
                c = True
                array[position] = array[position - 1]
            else:
                break
            position -= 1
        array[position] = currentValue

sort1(array)

for i in range(n):
    for el in array[i][0]:
        print(el,end = ' ')
    print('')
