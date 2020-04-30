n = int(input())
k = int(input())
array = list(range(0,n+1))

def w(x):
    l = map(int,list(str(x)))
    return sum(l)

def comp(x,y):
    if w(x) > w(y):
        return True
    if w(x) == w(y) and str(x) > str(y):
        return True
    return False

def sort1(array):
    n = len(array)
    for index in range(1, n):

        currentValue = array[index]
        position = index
        c = False
        while position > 0:
            if comp(array[position - 1],currentValue):
                c = True
                array[position] = array[position - 1]
            else:
                break
            position -= 1
        array[position] = currentValue

sort1(array)
#print(array)
print(array.index(k))
print(array[k])
