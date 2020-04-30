numbers = list(map(int, input().split()))
from itertools import permutations

def funk(arr, val, index):
    if index == 5:
        if val == 23:
            return True
        else:
            return False
    if funk(arr, val + arr[index], index + 1):
        return True
    if funk(arr, val - arr[index], index + 1):
        return True
    if funk(arr, val * arr[index], index + 1):
        return True
    return False

while any(numbers):
    perm = permutations(numbers, 5)
    for el in perm:
        res = funk(el,el[0],1)
        if res:
            break
    if res:
        print('Possible')
    else:
        print('Impossible')
    numbers = list(map(int, input().split()))
