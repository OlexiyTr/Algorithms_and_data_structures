st, m = input().split()

max = 0

def funk(arr,m,res=''):
    global max
    if m == 1:
        new_max = multiplyList(map(int,(res+' '+arr).split()))
        if max < new_max:
            max = new_max
        return
    for pos in range(1,len(arr)-m+2):
        funk(arr[pos:],m-1,res+' '+arr[:pos])

def multiplyList(myList) :
    result = 1
    for x in myList:
         result = result * x
    return result

while True:
    max = 0
    funk(st, int(m))
    print(max)
    try:
        st, m = input().split()
    except:
        break
