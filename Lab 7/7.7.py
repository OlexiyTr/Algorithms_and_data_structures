n = int(input())
array =list(map(int, input().split()))

def sort1(array):
    n = len(array)
    for index in range(1, n):

        currentValue = array[index]
        position = index
        c = False
        while position > 0:
            if array[position - 1] > currentValue:
                c = True
                array[position] = array[position - 1]
            else:
                break
            position -= 1
        array[position] = currentValue
        if c:
            for i in range(len(array)):
                print(array[i],end = ' ')
            print('')

sort1(array)
